document.addEventListener('DOMContentLoaded', function () {
    const messageBox = document.getElementsByClassName("message")[0];
    $('#messageContent').on('input', function (e) {
        currentMessage = e.target.value;
    });

    const handleChatData = async () => {
        if (currentMessage === "" || currentMessage === null || currentMessage === undefined) {
            console.log("Empty Message")
            return;
        } else {
            const userMessageContent = document.getElementById('messageContent');
    
            const userMessage = document.createElement('div');
            userMessage.id = `userMessage${usermessageCount}`;
            userMessage.classList.add("chat__box");
            userMessage.classList.add("bot__chat");
            userMessage.innerHTML = `
            <span class="author">User</span>
            </div>
            <div class="chat">
            <p>${userMessageContent.value}</p>
        `;
            usermessageCount++;
            botmessageCount++;
            messageBox.append(userMessage);
            userMessageContent.value = '';

            if (messages.length === 0) {
                const chatData = {
                    role: 'user',
                    content: currentMessage
                }
                currentMessage = '';
                messageData.push(chatData);
                dataToSend.messages.push(chatData);
                dataToSend.messages = [...dataToSend.messages, ...messageData];
                let finalMessage = '';
                fetch(
                    `https://api.runpod.ai/v2/${RP_CHAT_ID}/openai/v1/chat/completions`,
                    {
                        method: 'POST',
                        headers: {
                            'Authorization': `Bearer ${RP_CHAT_TOKEN}`,
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify(dataToSend),
                        timeout: 60000,
                    }
                )
                    .then((response) => {
                        const reader = response.body.getReader();
                        return new ReadableStream({
                            start(controller) {
                                return pump();
                                function pump() {
                                    return reader.read().then(({ done, value }) => {
                                        // When no more data needs to be consumed, close the stream
                                        if (done) {
                                            controller.close();
                                            return;
                                        }
                                        // Enqueue the next data chunk into our target stream
                                        controller.enqueue(value);
                                        return pump();
                                    });
                                }
                            },
                        });
                    })

                    .then((stream) => new Response(stream))
                    .then((response) => response.blob())
                    .then((blobdata) => blobdata.text())
                    .then((data) => {

                        let piece_buffer = data.split('\n\n');
                        let userChatContainer = document.createElement("div");
                        userChatContainer.id = `botMessage${botmessageCount}`;
                        userChatContainer.classList.add('chat__box');
                        userChatContainer.classList.add('your__chat');
                        messageBox.append(userChatContainer);
                        console.log("box    ", messageBox);
                        piece_buffer.forEach(element => {
                            if (element.includes('[DONE]')) return;
                            if (element.includes('data: ')) {
                                let piece = element.replace("data: ", "");
                                let jsonPiece = JSON.parse(piece);
                                const wordPiece = jsonPiece['choices'][0]['delta']['content'];
                                if (wordPiece) {
                                    const userChat = document.getElementById(`botMessage${botmessageCount}`);
                                    finalMessage += jsonPiece['choices'][0]['delta']['content'];
                                    if (userChat) {
                                        userChat.innerHTML = '';
                                        userChat.innerHTML = `
                                                <span class="author">Mirada AI</span>
                                                </div>
                                                <div class="chat">
                                                <p></p>
                                        `;
                                        const chatParagraph = userChat.querySelector('p');
                                        let currentIndex = 0;
                                        const displayNextWord = () => {
                                            if (currentIndex < finalMessage.length) {
                                                chatParagraph.textContent += finalMessage[currentIndex];
                                                currentIndex++;
                                                setTimeout(displayNextWord, 20); // Adjust the delay (in milliseconds) as needed
                                            }
                                        };
                                        displayNextWord();
                                    }
                                }
                            }
                        });
                    })
                    .then(() => {
                        messageData.push({
                            role: 'assistant',
                            content: finalMessage
                        })
                        console.log(messageData);
                    })
                    .catch((error) => {
                        console.error('Error:', error);
                    });
            }
        }
    }

    $('#sendMsgBtn').on('click', function () {
        handleChatData();
    })
    $('#messageContent').on('keydown', function (e) {
        if (e.key == "Enter") {
            handleChatData();
        }
    })
});
