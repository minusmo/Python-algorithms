

def hanoi(n):
    stick1 = [1, 2, 3];
    stick2 = [];
    stick3 = [];

    def move_rings(m, stick_1, stick_2, stick_3):
        if (m == 1):
            stick_3.append(stick_1.pop());
            print(stick_1, stick_2, stick_3);
            print("\n")
        else:
            move_rings(m-1, stick_1, stick_3, stick_2);
            stick_3.append(stick_1.pop());
            print(stick_1, stick_2, stick_3);
            print("\n");

            move_rings(m-1, stick_2, stick_1, stick_3);
            print(stick_1, stick_2, stick_3);
            print("\n");
        return stick_1, stick_2, stick_3;

    move_rings(n, stick1, stick2, stick3);

    print(stick1, stick2, stick3);
    return;


hanoi(3);

