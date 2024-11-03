let shrink = document.querySelector(".shrink")
let bgWall = document.querySelector(".bg-wall")
shrink.addEventListener('mouseenter',()=>{
    shrink.classList.add("shrink_active")
})
shrink.addEventListener('mouseleave',()=>{
    shrink.classList.remove("shrink_active")
})
shrink.addEventListener('click',()=>{
    bgWall.style.display="none"
})
