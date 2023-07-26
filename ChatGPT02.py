from ftplib import FTP

def get_ftp_file_list(ftp, path='.'):
    file_list = []
    ftp.cwd(path)
    ftp.retrlines('NLST', file_list.append)
    return file_list

def download_ftp_files(hostname, username, password, remote_path, local_path):
    try:
        with FTP(hostname) as ftp:
            ftp.login(username, password)
            ftp.cwd(remote_path)
            
            file_list = get_ftp_file_list(ftp)
            print(f"Found {len(file_list)} files: {file_list}")
            
            for file_name in file_list:
                remote_file_path = f"{remote_path}/{file_name}"
                local_file_path = f"{local_path}/{file_name}"
                
                with open(local_file_path, 'wb') as local_file:
                    ftp.retrbinary(f'RETR {remote_file_path}', local_file.write)
                
                print(f"Downloaded: {file_name}")
                
    except Exception as e:
        print(f"Error: {e}")

# Example usage:
hostname = 'ftp.example.com'
username = 'your_username'
password = 'your_password'
remote_path = '/remote/directory'  # Change this to the directory containing the files you want to download
local_path = '/local/directory'    # Change this to the local directory where you want to save the files

download_ftp_files(hostname, username, password, remote_path, local_path)
