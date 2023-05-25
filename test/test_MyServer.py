from demo_MyServer import MyServer


def main():
    s = MyServer('127.0.0.1', 23333)
    s.start_server()
    count = 0
    while count < 5:
        s.send_time()
        print('发送了', count)
        count += 1

    s.stop_server()
    print('stopped')


if __name__ == '__main__':
    main()
