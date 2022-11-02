import wifi
import socketpool
import adafruit_requests
import ssl
import os
from adafruit_httpserver import HTTPServer, HTTPResponse
import digitalio
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
import time


time.sleep(1)

# The keyboard object!
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

print("Connect Wifi")
wifi.radio.connect(os.getenv('WIFI_SSID'), os.getenv('WIFI_PASSWORD'))
print("Connected!")
print("IP ADDR:", str(wifi.radio.ipv4_address))

pool = socketpool.SocketPool(wifi.radio)
server = HTTPServer(pool)
server.request_buffer_size = 2048

def typing(key):
    keyboard.press(key)
    keyboard.release_all()

def wireless_keyboard(keystroke):
    print(keystroke)
    if keystroke == "enter":
        typing(Keycode.ENTER)
    elif keystroke == "space":
        typing(Keycode.SPACE)
    elif keystroke == "backspace":
        typing(Keycode.BACKSPACE)
    else:
        keyboard_layout.write(f"{keystroke}")
    time.sleep(0.3)


@server.route("/")
def base(request):  
    """Default reponse is /index.html"""	
    return HTTPResponse(filename="/index.html")


@server.route(f"/key/a")
def on_a(request):
	wireless_keyboard("a")
	return HTTPResponse(body=f"a")

@server.route(f"/key/b")
def on_b(request):
	wireless_keyboard("b")
	return HTTPResponse(body=f"b")

@server.route(f"/key/c")
def on_c(request):
	wireless_keyboard("c")
	return HTTPResponse(body=f"c")

@server.route(f"/key/d")
def on_d(request):
	wireless_keyboard("d")
	return HTTPResponse(body=f"d")

@server.route(f"/key/e")
def on_e(request):
	wireless_keyboard("e")
	return HTTPResponse(body=f"e")

@server.route(f"/key/f")
def on_f(request):
	wireless_keyboard("f")
	return HTTPResponse(body=f"f")

@server.route(f"/key/g")
def on_g(request):
	wireless_keyboard("g")
	return HTTPResponse(body=f"g")

@server.route(f"/key/h")
def on_h(request):
	wireless_keyboard("h")
	return HTTPResponse(body=f"h")

@server.route(f"/key/i")
def on_i(request):
	wireless_keyboard("i")
	return HTTPResponse(body=f"i")

@server.route(f"/key/j")
def on_j(request):
	wireless_keyboard("j")
	return HTTPResponse(body=f"j")

@server.route(f"/key/k")
def on_k(request):
	wireless_keyboard("k")
	return HTTPResponse(body=f"k")

@server.route(f"/key/l")
def on_l(request):
	wireless_keyboard("l")
	return HTTPResponse(body=f"l")

@server.route(f"/key/m")
def on_m(request):
	wireless_keyboard("m")
	return HTTPResponse(body=f"m")

@server.route(f"/key/n")
def on_n(request):
	wireless_keyboard("n")
	return HTTPResponse(body=f"n")

@server.route(f"/key/o")
def on_o(request): 
	wireless_keyboard("o")
	return HTTPResponse(body=f"o")

@server.route(f"/key/p")
def on_p(request):
	wireless_keyboard("p")
	return HTTPResponse(body=f"p")

@server.route(f"/key/q")
def on_q(request):
	wireless_keyboard("q")
	return HTTPResponse(body=f"q")

@server.route(f"/key/r")
def on_r(request):
	wireless_keyboard("r")
	return HTTPResponse(body=f"r")

@server.route(f"/key/s")
def on_s(request):
	wireless_keyboard("s")
	return HTTPResponse(body=f"s")

@server.route(f"/key/t")
def on_t(request):
	wireless_keyboard("t")
	return HTTPResponse(body=f"t")

@server.route(f"/key/u")
def on_u(request):
	wireless_keyboard("u")
	return HTTPResponse(body=f"u")

@server.route(f"/key/v")
def on_v(request): 
	wireless_keyboard("v")
	return HTTPResponse(body=f"v")

@server.route(f"/key/w")
def on_w(request):
	wireless_keyboard("w")
	return HTTPResponse(body=f"w")

@server.route(f"/key/x")
def on_x(request):
	wireless_keyboard("x")
	return HTTPResponse(body=f"x")

@server.route(f"/key/y")
def on_y(request):
	wireless_keyboard("y")
	return HTTPResponse(body=f"y")

@server.route(f"/key/z")
def on_z(request):
	wireless_keyboard("z")
	return HTTPResponse(body=f"z")

@server.route(f"/key/A")
def on_A(request):
	wireless_keyboard("A")
	return HTTPResponse(body=f"A")

@server.route(f"/key/B")
def on_B(request):
	wireless_keyboard("B")
	return HTTPResponse(body=f"B")

@server.route(f"/key/C")
def on_C(request): 
	wireless_keyboard("C")
	return HTTPResponse(body=f"C")

@server.route(f"/key/D")
def on_D(request):
	wireless_keyboard("D")
	return HTTPResponse(body=f"D")

@server.route(f"/key/E")
def on_E(request):
	wireless_keyboard("E")
	return HTTPResponse(body=f"E")

@server.route(f"/key/F")
def on_F(request):
	wireless_keyboard("F")
	return HTTPResponse(body=f"F")

@server.route(f"/key/G")
def on_G(request):
	wireless_keyboard("G")
	return HTTPResponse(body=f"G")

@server.route(f"/key/H")
def on_H(request): 
	wireless_keyboard("H")
	return HTTPResponse(body=f"H")

@server.route(f"/key/I")
def on_I(request):
	wireless_keyboard("I")
	return HTTPResponse(body=f"I")

@server.route(f"/key/J")
def on_J(request):
	wireless_keyboard("J")
	return HTTPResponse(body=f"J")

@server.route(f"/key/K")
def on_K(request):
	wireless_keyboard("K")
	return HTTPResponse(body=f"K")

@server.route(f"/key/L")
def on_L(request):
	wireless_keyboard("L")
	return HTTPResponse(body=f"L")

@server.route(f"/key/M")
def on_M(request):
	wireless_keyboard("M")
	return HTTPResponse(body=f"M")

@server.route(f"/key/N")
def on_N(request):
	wireless_keyboard("N")
	return HTTPResponse(body=f"N")

@server.route(f"/key/O")
def on_O(request):
	wireless_keyboard("O")
	return HTTPResponse(body=f"O")

@server.route(f"/key/P")
def on_P(request):
	wireless_keyboard("P")
	return HTTPResponse(body=f"P")

@server.route(f"/key/Q")
def on_Q(request):
	wireless_keyboard("Q")
	return HTTPResponse(body=f"Q")

@server.route(f"/key/R")
def on_R(request):
	wireless_keyboard("R")
	return HTTPResponse(body=f"R")

@server.route(f"/key/S")
def on_S(request):
	wireless_keyboard("S")
	return HTTPResponse(body=f"S")

@server.route(f"/key/T")
def on_T(request):
	wireless_keyboard("T")
	return HTTPResponse(body=f"T")

@server.route(f"/key/U")
def on_U(request):
	wireless_keyboard("U")
	return HTTPResponse(body=f"U")

@server.route(f"/key/V")
def on_V(request):
	wireless_keyboard("V")
	return HTTPResponse(body=f"V")

@server.route(f"/key/W")
def on_W(request):
	wireless_keyboard("W")
	return HTTPResponse(body=f"W")

@server.route(f"/key/X")
def on_X(request):
	wireless_keyboard("X")
	return HTTPResponse(body=f"X")

@server.route(f"/key/Y")
def on_Y(request):
	wireless_keyboard("Y")
	return HTTPResponse(body=f"Y")

@server.route(f"/key/Z")
def on_Z(request):
	wireless_keyboard("Z")
	return HTTPResponse(body=f"Z")

@server.route(f"/key/enter")
def on_enter(request):
	wireless_keyboard("enter")
	return HTTPResponse(body=f"enter")

@server.route(f"/key/space")
def on_space(request): 
	wireless_keyboard("space")
	return HTTPResponse(body=f"space")

@server.route(f"/key/backspace")
def on_backspace(request):
	wireless_keyboard("backspace")
	return HTTPResponse(body=f"backspace")

server.serve_forever(str(wifi.radio.ipv4_address))