let navFlag = false; 
let sideFlag = false

document.addEventListener('DOMContentLoaded', function() {
    $('#fullscreenBtn').on('click', async function() {
        await window.resizeEvent.resizeWindow();
    });

    const selectButtons = document.getElementById("nav-content").querySelectorAll(".navContentDiv");

    selectButtons.forEach((element) => {
        
        element.addEventListener('click', function() {
            selectButtons.forEach((element) => element.style.backgroundColor = '');
            element.style.backgroundColor = '#3d3d3d';
            let currentId = element.id;
            document.querySelectorAll(".nav-page").forEach((item) => item.classList.add('hidden-page'));
            document.getElementById(`${currentId}-page`).classList.remove('hidden-page');
            if(currentId == "nav-image" || currentId == "nav-notes") {
                $(".side-bar").css('display', 'none');
            } else {
                $(".side-bar").css('display', 'flex');
            }
        })
    });

    $('#collapseBtn').on('click', function() {
        if (navFlag) {
            $('.nav-bar').css('width', '20%');
            $('#nav-content').show();
            $('#nav-setting').show();
            $(this).html('&nbsp;&lt;'); // Change content to '&lt;'
            navFlag = false;
        } else {
            $('.nav-bar').css('width', '0%');
            $('#nav-content').hide();
            $('#nav-setting').hide();
            $(this).html('&nbsp;&gt;'); // Change content to '&gt;'
            navFlag = true;
        }
    })
    $('#collapseSidebarBtn').on('click', function() {
        if (sideFlag) {
            $('.side-bar').css('width', '0%');
            $('#newChat').css('display', 'none');
            $(this).css('right', '5%')
            $(this).html('&nbsp;&lt;'); // Change content to '&lt;'
            sideFlag = false;
        } else {
            $('.side-bar').css('width', '20%');
            $('#newChat').css('display', 'flex');
            $(this).html('&nbsp;&gt;');
            $(this).css('right', '23%') // Change content to '&gt;'
            sideFlag = true;
        }
    })
});