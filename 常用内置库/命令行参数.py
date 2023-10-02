'''
为了简化参数解析，我们可以使用内置的argparse库，定义好各个参数类型后，它能直接返回有效的参数。
argparse支持参数检查
argparse支持设置默认值
缺少必要的参数，或者参数不对，将报告详细的错误信息
更神奇的是，如果输入-h，则打印帮助信息
'''
import argparse


def main():
    # 定义一个ArgumentParser实例:
    parser = argparse.ArgumentParser(
        prog='backup',  # 程序名
        description='Backup MySQL database.',  # 描述
        epilog='Copyright(r), 2023'  # 说明信息
    )
    # 定义位置参数:
    parser.add_argument('outfile')
    # 定义关键字参数:
    parser.add_argument('--host', default='localhost')
    # 此参数必须为int类型:
    parser.add_argument('--port', default='3306', type=int)
    # 允许用户输入简写的-u:
    parser.add_argument('-u', '--user', required=True)
    parser.add_argument('-p', '--password', required=True)
    parser.add_argument('--database', required=True)
    # gz参数不跟参数值，因此指定action='store_true'，意思是出现-gz表示True:
    parser.add_argument('-gz', '--gzcompress', action='store_true', required=False, help='Compress backup files by gz.')

    # 解析参数:
    args = parser.parse_args()

    # 打印参数:
    print('parsed args:')
    print(f'outfile = {args.outfile}')
    print(f'host = {args.host}')
    print(f'port = {args.port}')
    print(f'user = {args.user}')
    print(f'password = {args.password}')
    print(f'database = {args.database}')
    print(f'gzcompress = {args.gzcompress}')


if __name__ == '__main__':
    main()

'''
$ ./backup.py -u root -p hello --database testdb backup.sql
parsed args:
outfile = backup.sql
host = localhost
port = 3306
user = root
password = hello
database = testdb
gzcompress = False
'''
