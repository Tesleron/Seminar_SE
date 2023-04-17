import pyttsx3
import time
import math

engine = pyttsx3.init()

def yp(n, m, k, view, interval, i = 0):
    message = ""
    # 0<n     n elements in the circle
    # 1<=m<=n    reduce the m element after the current existing element
    # 1<=k<=n k elements remain in the circle at the end of process
    # print("n =", n, " m =", m, " k =", k)
    if view.checkbox_var.get() is True:
        i = n - i - 1
    l = [i for i in range(1, n+1)]
    while (len(l) > k and view.active):
        view.playButton.config(state='disabled')
        view.sliderPeople.config(state='disabled')
        i = (i + m) % len(l)
        j = len(l) - i - 1
        if view.checkbox_var.get() is False:
            view.remove_numbers(l[i])
            l.remove(l[i])
        else:
            # print(f"l is \n{l}\nj is\n{j}\nl[j] is \n{l[j]}\nview.numbers is\n{view.numbers}\n")
            view.remove_numbers(l[j])
            l.remove(l[j])
        view.master.update()
        time.sleep(interval/2)
    view.playButton.config(state='active')
    view.sliderPeople.config(state='active')
    if m == 1 and k==1 and view.active and view.checkbox_var.get() is False:
     message = "n = " + str(n) + " survive by algorithm = " + str(l) + ", survive by formula = " + str(int(2 * (n - math.pow(2, math.floor(math.log(n, 2)))) + 1))
     view.display_endgame_msg(message)
    #  print("n =", n, "survive by algorithm =", l, \
    #        "survive by formula =", \
    #        int(2 * (n - math.pow(2, math.floor(math.log(n, 2)))) + 1))
    elif view.active:
        message = "n = " + str(n) + " survive by algorithm = " + str(l)
        view.display_endgame_msg(message)
        # print("n =", n, "survive by algorithm =", l)
    else:
        pass
    engine.say(message)
        # say method on the engine that passing input text to be spoken
    
    # run and wait method, it processes the voice commands.
    engine.runAndWait()
        # print("Game canceled")

        