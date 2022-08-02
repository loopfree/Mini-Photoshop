const socket = io()

socket.on("change-image", (new_image) =>{
    image_display.src = new_image
})