from Connectivity import IBApp


if __name__ == '__main__':
    app = IBApp("127.0.0.1", 7497, 10)

    current_time = app.speaking_clock()
 
    print(current_time)

    app.disconnect()
