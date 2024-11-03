let server = document.querySelectorAll(".server")
for (let i = 0; i < server.length; i++) {
    server[i].addEventListener('mouseenter', () => {
        server[i].classList.add('server_active')
        // server[i].classList.remove('shadow')
        server[i].classList.add('shadow_active')
        server[i].nextElementSibling.classList.add('server_name_active')
    })
    server[i].addEventListener('mouseleave', () => {
        server[i].classList.remove('server_active')
        // server[i].classList.add('shadow')
        server[i].classList.remove('shadow_active')
        server[i].nextElementSibling.classList.remove('server_name_active')
    })
}