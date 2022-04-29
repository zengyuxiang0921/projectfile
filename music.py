import pyaudio
import wave
run=True
while run:
    if __name__=="__main__":
        filename=input("open:")
        chunk=1024
        try:
            wf = wave.open(filename, 'rb')
        except wave.Error:
            print("This file isn't a wave file.Please try a wave file")
            continue
        except KeyboardInterrupt:
            continue
        p=pyaudio.PyAudio()
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)
        data=wf.readframes(chunk)
        while data !='':
            stream.write(data)
            data=wf.readframes(chunk)
        stream.close()
        p.terminate()