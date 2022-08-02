//upload and download buttons
image_input.addEventListener("change", (e) => {
    const fileReader = new FileReader()

    fileReader.onload = () => {
        image_display.src = fileReader.result

        socket.emit("submit-image", {
            "image-data": fileReader.result
        })
    }

    fileReader.readAsDataURL(e.target.files[0])
})

const modifier_btns = document.getElementsByClassName("modifier-btn")
for(let i = 0; i < modifier_btns.length; ++i) {
    const btn = modifier_btns[i]

    const temp = btn.name
    const emit_str = temp.substring(0, temp.indexOf("-"))
    btn.addEventListener("click", () => {
        socket.emit(`${emit_str}-image`, {
            "image-data": image_display.src
        })
    })
}

// const reset_btn = document.getElementsByName("reset-btn")[0]
// reset_btn.addEventListener("click", () => {
//     socket.emit("reset-image")
// })

// //milestone 1
// const invert_btn = document.getElementsByName("invert-btn")[0]

// invert_btn.addEventListener("click", () => {
//     socket.emit("invert-image", {
//         "image-data": image_display.src
//     })
// })

// const grayscale_btn = document.getElementsByName("grayscale-btn")[0]

// grayscale_btn.addEventListener("click", () => {
//     socket.emit("grayscale-image", {
//         "image-data": image_display.src
//     })
// })

// const complement_btn = document.getElementsByName("complement-btn")[0]

// complement_btn.addEventListener("click", () => {
//     socket.emit("complement-image", {
//         "image-data": image_display.src
//     })
// })

// const flipleft_btn = document.getElementsByName("flipleft-btn")[0]

// flipleft_btn.addEventListener("click", () => {
//     socket.emit("flipleft-image", {
//         "image-data": image_display.src
//     })
// })