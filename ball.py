import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('34.68.81.63', 6666))
while True:
    receivedata = s.recv(1024).decode('utf-8')
    print("[+]receivedata=", receivedata)
    receivedata = s.recv(1024).decode('utf-8')
    print("[+]receivedata=", receivedata)
    s.sendall(("1,2,3,4 5,6,7,8"+"\n").encode("utf-8"))
    print("[+]senddata=", "1,2,3,4 5,6,7,8")
    receivedata = s.recv(1024).decode('utf-8')
    print("[+]receivedata=", receivedata)

    while True:
        if "Both" in receivedata:
            receivedata = s.recv(1024).decode('utf-8')
            print("[+]receivedata=", receivedata)
            s.sendall(("1,2 9,10"+"\n").encode("utf-8"))
            print("[+]senddata=", "1,2 9,10")
            receivedata = s.recv(1024).decode('utf-8')
            print("[+]receivedata=", receivedata)
            if "Both" in receivedata:
                receivedata = s.recv(1024).decode('utf-8')
                print("[+]receivedata=", receivedata)
                s.sendall(("1 11"+"\n").encode("utf-8"))
                print("[+]senddata=", "1 11")
                receivedata = s.recv(1024).decode('utf-8')
                print("[+]receivedata=", receivedata)
                if "Both" in receivedata:
                    receivedata = s.recv(1024).decode('utf-8')
                    print("[+]receivedata=", receivedata)
                    s.sendall(("12" + "\n").encode("utf-8"))
                    print("[+]senddata=", "12")
                    break
                else:
                    receivedata = s.recv(1024).decode('utf-8')
                    print("[+]receivedata=", receivedata)
                    s.sendall(("11"+"\n").encode("utf-8"))
                    print("[+]senddata=", "11")
                    break
            else:
                receivedata = s.recv(1024).decode('utf-8')
                print("[+]receivedata=", receivedata)
                s.sendall(("1 9" + "\n").encode("utf-8"))
                print("[+]senddata=", "1 9")
                receivedata = s.recv(1024).decode('utf-8')
                print("[+]receivedata=", receivedata)
                if "Both" in receivedata:
                    receivedata = s.recv(1024).decode('utf-8')
                    print("[+]receivedata=", receivedata)
                    s.sendall(("10"+"\n").encode("utf-8"))
                    print("[+]senddata=", "10")
                    break
                else:
                    receivedata = s.recv(1024).decode('utf-8')
                    print("[+]receivedata=", receivedata)
                    s.sendall(("9"+"\n").encode("utf-8"))
                    print("[+]senddata=", "9")
                    break

        if "lighter" in receivedata:
            receivedata = s.recv(1024).decode('utf-8')
            print("[+]receivedata=", receivedata)
            s.sendall(("1,2,9 3,4,5" + "\n").encode("utf-8"))
            print("[+]senddata=", "1,2,9 3,4,5")
            receivedata = s.recv(1024).decode('utf-8')
            print("[+]receivedata=", receivedata)
            if "Both" in receivedata:
                receivedata = s.recv(1024).decode('utf-8')
                print("[+]receivedata=", receivedata)
                s.sendall(("6 7"+"\n").encode("utf-8"))
                print("[+]senddata=", "6 7")
                receivedata = s.recv(1024).decode('utf-8')
                print("[+]receivedata=", receivedata)
                if "Both" in receivedata:
                    receivedata = s.recv(1024).decode('utf-8')
                    print("[+]receivedata=", receivedata)
                    s.sendall(("8"+"\n").encode("utf-8"))
                    print("[+]senddata=", "8")
                    break
                if "lighter" in receivedata:
                    receivedata = s.recv(1024).decode('utf-8')
                    print("[+]receivedata=", receivedata)
                    s.sendall(("7" + "\n").encode("utf-8"))
                    print("[+]senddata=", "7")
                    break
                if "heavier" in receivedata:
                    receivedata = s.recv(1024).decode('utf-8')
                    print("[+]receivedata=", receivedata)
                    s.sendall(("6"+"\n").encode("utf-8"))
                    print("[+]senddata=", "6")
                    break
            if "lighter" in receivedata:
                receivedata = s.recv(1024).decode('utf-8')
                print("[+]receivedata=", receivedata)
                s.sendall(("1 2" + "\n").encode("utf-8"))
                print("[+]senddata=", "1 2")
                receivedata = s.recv(1024).decode('utf-8')
                print("[+]receivedata=", receivedata)
                if "Both" in receivedata:
                    receivedata = s.recv(1024).decode('utf-8')
                    print("[+]receivedata=", receivedata)
                    s.sendall(("5"+"\n").encode("utf-8"))
                    print("[+]senddata=", "5")
                    break
                if "lighter" in receivedata:
                    receivedata = s.recv(1024).decode('utf-8')
                    print("[+]receivedata=", receivedata)
                    s.sendall(("1" + "\n").encode("utf-8"))
                    print("[+]senddata=", "1")
                    break
                if "heavier" in receivedata:
                    receivedata = s.recv(1024).decode('utf-8')
                    print("[+]receivedata=", receivedata)
                    s.sendall(("2"+"\n").encode("utf-8"))
                    print("[+]senddata=", "2")
                    break
            if "heavier" in receivedata:
                receivedata = s.recv(1024).decode('utf-8')
                print("[+]receivedata=", receivedata)
                s.sendall(("3 4" + "\n").encode("utf-8"))
                print("[+]senddata=", "3 4")
                receivedata = s.recv(1024).decode('utf-8')
                print("[+]receivedata=", receivedata)
                if "lighter" in receivedata:
                    receivedata = s.recv(1024).decode('utf-8')
                    print("[+]receivedata=", receivedata)
                    s.sendall(("3" + "\n").encode("utf-8"))
                    print("[+]senddata=", "3")
                    break
                if "heavier" in receivedata:
                    receivedata = s.recv(1024).decode('utf-8')
                    print("[+]receivedata=", receivedata)
                    s.sendall(("4"+"\n").encode("utf-8"))
                    print("[+]senddata=", "4")
                    break

        if "heavier" in receivedata:
            receivedata = s.recv(1024).decode('utf-8')
            print("[+]receivedata=", receivedata)
            s.sendall(("1,2,9 3,4,5" + "\n").encode("utf-8"))
            print("[+]senddata=", "1,2,9 3,4,5")
            receivedata = s.recv(1024).decode('utf-8')
            print("[+]receivedata=", receivedata)
            if "Both" in receivedata:
                receivedata = s.recv(1024).decode('utf-8')
                print("[+]receivedata=", receivedata)
                s.sendall(("6 7"+"\n").encode("utf-8"))
                print("[+]senddata=", "6 7")
                receivedata = s.recv(1024).decode('utf-8')
                print("[+]receivedata=", receivedata)
                if "Both" in receivedata:
                    receivedata = s.recv(1024).decode('utf-8')
                    print("[+]receivedata=", receivedata)
                    s.sendall(("8"+"\n").encode("utf-8"))
                    print("[+]senddata=", "8")
                    break
                if "lighter" in receivedata:
                    receivedata = s.recv(1024).decode('utf-8')
                    print("[+]receivedata=", receivedata)
                    s.sendall(("6" + "\n").encode("utf-8"))
                    print("[+]senddata=", "6")
                    break
                if "heavier" in receivedata:
                    receivedata = s.recv(1024).decode('utf-8')
                    print("[+]receivedata=", receivedata)
                    s.sendall(("7"+"\n").encode("utf-8"))
                    print("[+]senddata=", "7")
                    break
            if "heavier" in receivedata:
                receivedata = s.recv(1024).decode('utf-8')
                print("[+]receivedata=", receivedata)
                s.sendall(("1 2" + "\n").encode("utf-8"))
                print("[+]senddata=", "1 2")
                receivedata = s.recv(1024).decode('utf-8')
                print("[+]receivedata=", receivedata)
                if "Both" in receivedata:
                    receivedata = s.recv(1024).decode('utf-8')
                    print("[+]receivedata=", receivedata)
                    s.sendall(("5"+"\n").encode("utf-8"))
                    print("[+]senddata=", "5")
                    break
                if "lighter" in receivedata:
                    receivedata = s.recv(1024).decode('utf-8')
                    print("[+]receivedata=", receivedata)
                    s.sendall(("2" + "\n").encode("utf-8"))
                    print("[+]senddata=", "2")
                    break
                if "heavier" in receivedata:
                    receivedata = s.recv(1024).decode('utf-8')
                    print("[+]receivedata=", receivedata)
                    s.sendall(("1"+"\n").encode("utf-8"))
                    print("[+]senddata=", "1")
                    break
            if "lighter" in receivedata:
                receivedata = s.recv(1024).decode('utf-8')
                print("[+]receivedata=", receivedata)
                s.sendall(("3 4" + "\n").encode("utf-8"))
                print("[+]senddata=", "3 4")
                receivedata = s.recv(1024).decode('utf-8')
                print("[+]receivedata=", receivedata)
                if "lighter" in receivedata:
                    receivedata = s.recv(1024).decode('utf-8')
                    print("[+]receivedata=", receivedata)
                    s.sendall(("4" + "\n").encode("utf-8"))
                    print("[+]senddata=", "4")
                    break
                if "heavier" in receivedata:
                    receivedata = s.recv(1024).decode('utf-8')
                    print("[+]receivedata=", receivedata)
                    s.sendall(("3"+"\n").encode("utf-8"))
                    print("[+]senddata=", "3")
                    break
