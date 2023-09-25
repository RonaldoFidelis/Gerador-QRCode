import qrcode
import qrcode_terminal

def createPng_qrcode(data, name_file='qrcode'):

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    img.save(f'{name_file}.png')

    img.show()


def show_qrcode(data):
    qr = qrcode_terminal
    qr.draw(data)


def main():
    print("===========================")
    print("     Gerador de QRCode     ")
    print("===========================\n")

    condition = True

    while condition:
        print('Digite a URL')
        data = input('> ')

        if data == '':
            print('URL invalida.\nDigite novamente.')
            continue

        show_qrcode(data)

        print('Criar PNG? [s]sim [n]não')
        check_name = input('> ')

        if check_name == 'sim' or check_name == 's':
            print('Nome do QRCode:')
            name_file = input('> ')

            if name_file == '':
                createPng_qrcode(data)
                print('QRCode criado.\n')
            else:
                createPng_qrcode(data, name_file)
                print('QRCode criado.\n')
            
        print('[C]Criar novo QRCode [E]Sair do programa')
        check_continue = input('> ')

        if check_continue.lower() == 'e':
            print('Encerrando programa.')
            condition = False
        else:
            continue


if __name__ == "__main__":
    main()
