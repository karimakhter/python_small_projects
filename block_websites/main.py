import argparse

import yaml


def append_website_to_file( FILE, ADDRESS ):
    flag = False
    for itr in ADDRESS:

        with open( FILE, "r+" ) as filedata:
            for line in filedata.readlines():
                if line == f'127.0.0.1 {itr}\n':
                    flag = True
                    break
                if line != f'127.0.0.1 {itr}\n':
                    flag = False
                    continue
            if flag == False:
                filedata.writelines( f'127.0.0.1 {itr}\n' )
        filedata.close()


def delete_website_from_file( FILE, ADDRESS ):
    for itr in ADDRESS:
        with open( FILE, "r" ) as filedata:
            lines = filedata.readlines()
            filedata.close()
        with open( FILE, "w" ) as filedata:
            for line in lines:
                if line.strip( "\n" ) != f"127.0.0.1 {itr}":
                    filedata.write( line )


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument( '--action', help="BLOCK to block sitees, UNBLOCK to unblock sites" )
    args = parser.parse_args()

    with open( "./block_unblock_sites.yaml", "r" ) as sites:
        data = yaml.load( sites, Loader=yaml.FullLoader )
    sites.close()
    TO_BLOCK = data.get( "TO_BLOCK" )
    TO_DELETE = data.get( "TO_DELETE" )
    FILE = data.get( "FILE" )

    if args.action == "BLOCK":
        append_website_to_file( FILE=FILE, ADDRESS=TO_BLOCK )
    elif args.action == "UNBLOCK":
        delete_website_from_file( FILE=FILE, ADDRESS=TO_DELETE )
    else:
        print( "Please Provide correct argument" )
