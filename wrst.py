from datetime import datetime as dt

print('Start - Time Stamp > ', end='')
print(dt.today())


def if_exs(file_name: str = 'log.md'):
    """
    sub module for mk_fil
    """
    fn = file_name
    try:
        with open(fn, 'r') as check:
            file = check.read()
            print(f'- {fn} File exist.')
            # print(file)
            return 0
    except:
        print(f'- there is no file such {fn}')
        print('initiate create one')
        msg = 'Create - Time Stamp _> ' + str(dt.today()) + '\n'
        x = open(fn, 'w')
        print(f'- {msg}')
        x.write(msg)
        return 1


def mk_fil(file_name: str = 'log.md'):
    """
    Write/Read SPEED Test...
    """
    fn = file_name
    x = 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 525288, 1048576
    # a = x[9]
    a = 2048  # size to write
    sur = '00000000000000000000000000000000000000000000000000'

    if_ques = if_exs(fn)  # call made in function 'if_exs()'
    if if_ques:
        with open(fn, 'a') as file:
            ts = dt.today()  # time stamp - Start
            srt = 'Starting write: ' + str(ts) + '\n'
            print(srt)
            file.write(srt)
            for i in range(a):
                file.write('\n')
                for j in range(a):
                    file.write(sur)  # file to write
            te = dt.today()  # time stamp - End
            ert = '\nWrite end. ' + str(te) + '\n'
            print(ert)
            file.write(ert)


mk_fil()
