# This record keystrokes, and then appends that recording to a file 'keystroke_log.txt'.
# Currently it only exits upon hitting the escape key. Otherwise, I have tried it with
# every key on my keyboard, and only a few fall through the cracks (mostly the function keys).
import keyboard

def keystroke_tracker():
    recording = str(keyboard.record(until=chr(27)))
    translation = ''

    i = 0
    while i < len(recording):
        if recording[i:i + 5] == " up),":
            if recording[i - 7:i] == 't(space':
                translation += " "
            elif recording[i - 5:i] == 't(tab':
                translation += "\t"
            elif recording[i - 7:i] == 't(enter':
                translation += '\n'
            elif recording[i - 8:i] == 't(delete':
                translation += ' (delete) '
            elif recording[i - 11:i] == 't(backspace':
                translation += ' (backspace) '
            elif (recording[i - 7:i] == 't(shift' or recording[i - 4:i] == '(alt' or recording[
                                                                                     i - 5:i] == '(ctrl' or recording[
                                                                                                            i - 11:i] == '(right ctrl' or
                  recording[i - 6:i] == 't(down' or recording[i - 4:i] == 't(up' or recording[
                                                                                    i - 7:i] == 't(right' or recording[
                                                                                                             i - 6:i] == 't(left' or
                  recording[i - 12:i] == '(right shift' or recording[i - 11:i] == 't(caps lock' or recording[
                                                                                                   i - 10:i] == '(right alt' or
                  recording[i - 13:i] == '(left windows' or recording[i - 9:i] == 't(windows' or recording[
                                                                                                 i - 6:i] == 't(home' or recording[
                                                                                                                         i - 5:i] == 't(end' or
                  recording[i - 9:i] == 't(page up' or recording[i - 11:i] == 't(page down' or recording[
                                                                                               i - 10:i] == 't(num lock'):
                translation += ""
            else:
                translation += recording[i - 1]
        i += 1

    translation += '\n'
    translation += '\n'
    log = open('keystroke_log.txt', 'a')
    log.write(translation)
    log.close()

    print(recording)
    print("I'm done!")
