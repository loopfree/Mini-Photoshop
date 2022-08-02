from flask import Flask, render_template, request, send_from_directory
from flask_socketio import SocketIO, emit

from conversion import arr_to_pil, base64_to_arr, pil_to_base64
from milestone1 import flip_left_right, flip_up_down, rot_left, rot_right, grayscale, komplemen, negatif, zoom_in, zoom_out
from milestone2 import brightening_image, contrast_stretching, transformasi_log, transformasi_pangkat
from milestone3 import gaussian_blur, sharpening

app = Flask(__name__, template_folder="frontend")
socketio = SocketIO(app, max_http_buffer_size=50_000_000)

'''
    the dictionary will contain the following:
    key = request.sid
    value = original image in Base64 format
'''
client_data = {}

#helper function
def base64_shave(data: str):
    first_comma = data.find(",")
    return data[first_comma:len(data)]

#https functions
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/css/<path:path>")
def send_css(path):
    return send_from_directory("frontend/css", path)

@app.route("/js/<path:path>")
def send_js(path):
    return send_from_directory("frontend/js", path)


@app.route("/res/<path:path>")
def send_res(path):
    return send_from_directory("frontend/res", path)

#websocket functions
@socketio.on("connect")
def on_connect():
    print(f"{request.sid} connected")
    client_data[request.sid] = None

@socketio.on("disconnect")
def on_disconnect():
    print(f"{request.sid} disconnected")
    client_data.pop(request.sid)

@socketio.on("submit-image")
def on_submit_image(json):
    client_data[request.sid] = json["image-data"]

@socketio.on("reset-image")
def on_reset_image(json):
    emit("change-image", client_data[request.sid])

@socketio.on("invert-image")
def on_invert_image(json):
    print("inverting-image")
    print("shaving base64")
    shaved = base64_shave(json["image-data"])

    print("converting base64 to array")
    converted = base64_to_arr(shaved)

    print(len(converted))
    print(len(converted[0]))

    print("inverting image")
    inverted = negatif(converted)

    print("convert array to pil")
    pil_image = arr_to_pil(inverted)

    print("turn pil to base64 string")
    base64_img = pil_to_base64(pil_image)
    base64_img = "data:image/png;base64," + base64_img

    print("sending back changed image")
    emit("change-image", base64_img)

@socketio.on("grayscale-image")
def on_grayscale_image(json):
    print("grayscaling-image")
    print("shaving base64")
    shaved = base64_shave(json["image-data"])

    print("converting base64 to array")
    converted = base64_to_arr(shaved)

    print("grayscale image")
    result = grayscale(converted)

    print("convert array to pil")
    pil_image = arr_to_pil(result)

    print("turn pil to base64 string")
    base64_img = pil_to_base64(pil_image)
    base64_img = "data:image/png;base64," + base64_img

    print("sending back changed image")
    emit("change-image", base64_img)

@socketio.on("complement-image")
def on_complement_image(json):
    print("complementing-image")
    print("shaving base64")
    shaved = base64_shave(json["image-data"])

    print("converting base64 to array")
    converted = base64_to_arr(shaved)

    print("complement image")
    result = komplemen(converted)

    print("convert array to pil")
    pil_image = arr_to_pil(result)

    print("turn pil to base64 string")
    base64_img = pil_to_base64(pil_image)
    base64_img = "data:image/png;base64," + base64_img

    print("sending back changed image")
    emit("change-image", base64_img)

@socketio.on("rotleft-image")
def on_rotleft_image(json):
    print("shaving base64")
    shaved = base64_shave(json["image-data"])

    print("converting base64 to array")
    converted = base64_to_arr(shaved)

    print("rotate left image")
    result = rot_left(converted)

    print("convert array to pil")
    pil_image = arr_to_pil(result)

    print("turn pil to base64 string")
    base64_img = pil_to_base64(pil_image)
    base64_img = "data:image/png;base64," + base64_img

    print("sending back changed image")
    emit("change-image", base64_img)

@socketio.on("rotright-image")
def on_rotright_image(json):
    print("complementing-image")
    print("shaving base64")
    shaved = base64_shave(json["image-data"])

    print("converting base64 to array")
    converted = base64_to_arr(shaved)

    print("rotate right image")
    result = rot_right(converted)

    print("convert array to pil")
    pil_image = arr_to_pil(result)

    print("turn pil to base64 string")
    base64_img = pil_to_base64(pil_image)
    base64_img = "data:image/png;base64," + base64_img

    print("sending back changed image")
    emit("change-image", base64_img)

@socketio.on("fliplr-image")
def on_flip_left_right_image(json):
    print("complementing-image")
    print("shaving base64")
    shaved = base64_shave(json["image-data"])

    print("converting base64 to array")
    converted = base64_to_arr(shaved)

    print("flip left right image")
    result = flip_left_right(converted)

    print("convert array to pil")
    pil_image = arr_to_pil(result)

    print("turn pil to base64 string")
    base64_img = pil_to_base64(pil_image)
    base64_img = "data:image/png;base64," + base64_img

    print("sending back changed image")
    emit("change-image", base64_img)

@socketio.on("flipud-image")
def on_flip_up_down_image(json):
    print("complementing-image")
    print("shaving base64")
    shaved = base64_shave(json["image-data"])

    print("converting base64 to array")
    converted = base64_to_arr(shaved)

    print("flip up down image")
    result = flip_up_down(converted)

    print("convert array to pil")
    pil_image = arr_to_pil(result)

    print("turn pil to base64 string")
    base64_img = pil_to_base64(pil_image)
    base64_img = "data:image/png;base64," + base64_img

    print("sending back changed image")
    emit("change-image", base64_img)

@socketio.on("zoomin-image")
def on_zoomin_image(json):
    print("shaving base64")
    shaved = base64_shave(json["image-data"])

    print("converting base64 to array")
    converted = base64_to_arr(shaved)

    print("zoomin image")
    result = zoom_in(converted)

    print("convert array to pil")
    pil_image = arr_to_pil(result)

    print("turn pil to base64 string")
    base64_img = pil_to_base64(pil_image)
    base64_img = "data:image/png;base64," + base64_img

    print("sending back changed image")
    emit("change-image", base64_img)

@socketio.on("zoomout-image")
def on_zoomout_image(json):
    print("shaving base64")
    shaved = base64_shave(json["image-data"])

    print("converting base64 to array")
    converted = base64_to_arr(shaved)

    print("zoomout image")
    result = zoom_out(converted)

    print("convert array to pil")
    pil_image = arr_to_pil(result)

    print("turn pil to base64 string")
    base64_img = pil_to_base64(pil_image)
    base64_img = "data:image/png;base64," + base64_img

    print("sending back changed image")
    emit("change-image", base64_img)

@socketio.on("brightening-image")
def on_brightening_image(json):
    print("shaving base64")
    shaved = base64_shave(json["image-data"])

    print("converting base64 to array")
    converted = base64_to_arr(shaved)

    print("brightening image")
    result = brightening_image(converted)

    print("convert array to pil")
    pil_image = arr_to_pil(result)

    print("turn pil to base64 string")
    base64_img = pil_to_base64(pil_image)
    base64_img = "data:image/png;base64," + base64_img

    print("sending back changed image")
    emit("change-image", base64_img)


@socketio.on("contrasting-image")
def on_contrasting_image(json):
    print("shaving base64")
    shaved = base64_shave(json["image-data"])

    print("converting base64 to array")
    converted = base64_to_arr(shaved)

    print("contrasting image")
    result = contrast_stretching(converted)

    print("convert array to pil")
    pil_image = arr_to_pil(result)

    print("turn pil to base64 string")
    base64_img = pil_to_base64(pil_image)
    base64_img = "data:image/png;base64," + base64_img

    print("sending back changed image")
    emit("change-image", base64_img)

@socketio.on("logtrans-image")
def on_transformasi_log_image(json):
    print("shaving base64")
    shaved = base64_shave(json["image-data"])

    print("converting base64 to array")
    converted = base64_to_arr(shaved)

    print("log transing image")
    result = transformasi_log(converted)

    print("convert array to pil")
    pil_image = arr_to_pil(result)

    print("turn pil to base64 string")
    base64_img = pil_to_base64(pil_image)
    base64_img = "data:image/png;base64," + base64_img

    print("sending back changed image")
    emit("change-image", base64_img)


@socketio.on("exptrans-image")
def on_transformasi_pangkat_image(json):
    print("shaving base64")
    shaved = base64_shave(json["image-data"])

    print("converting base64 to array")
    converted = base64_to_arr(shaved)

    print("exp transing image")
    result = transformasi_pangkat(converted)

    print("convert array to pil")
    pil_image = arr_to_pil(result)

    print("turn pil to base64 string")
    base64_img = pil_to_base64(pil_image)
    base64_img = "data:image/png;base64," + base64_img

    print("sending back changed image")
    emit("change-image", base64_img)

@socketio.on("gaussianblur-image")
def on_gaussianblur_image(json):
    print("shaving base64")
    shaved = base64_shave(json["image-data"])

    print("converting base64 to array")
    converted = base64_to_arr(shaved)

    print("Gaussian Blur image")
    result = gaussian_blur(converted)

    print("convert array to pil")
    pil_image = arr_to_pil(result)

    print("turn pil to base64 string")
    base64_img = pil_to_base64(pil_image)
    base64_img = "data:image/png;base64," + base64_img

    print("sending back changed image")
    emit("change-image", base64_img) 

@socketio.on("sharpening-image")
def on_sharpening_image(json):
    print("shaving base64")
    shaved = base64_shave(json["image-data"])

    print("converting base64 to array")
    converted = base64_to_arr(shaved)

    print("Sharpening image")
    result = sharpening(converted)

    print("convert array to pil")
    pil_image = arr_to_pil(result)

    print("turn pil to base64 string")
    base64_img = pil_to_base64(pil_image)
    base64_img = "data:image/png;base64," + base64_img

    print("sending back changed image")
    emit("change-image", base64_img) 

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=8000, debug=True)