from shared_imports import *

def progress_bar(file_list, text, pdf_merger):
    with click.progressbar(file_list, label=text) as bar:
        for pdf_file in bar:
            if os.path.getsize(pdf_file) > 0:
                pdf_merger.append(pdf_file)

def ensure_exclusivity(directory, current, file):
    if sum([bool(directory), bool(current), bool(file)]) > 1:
        click.echo(click.style("Error: Please provide only one of '-d', '-c', or '-f'", fg='red'))
        sys.exit(1)

def change_extension(file):
    if not file.endswith('.pdf'):
        file += '.pdf'
    return file

def save_output(file, pdf_merger):
    with open(file, 'wb') as output_file:
        pdf_merger.write(output_file)

def handle_invalid_files(list):
    if list:
        invalid_files_str = ', '.join(list)
        click.echo(click.style(f"Error: Invalid value for '-f' / '--file': Path '{invalid_files_str}' {'do' if len(list) > 1 else 'does'} not exist.",fg='red'))
        sys.exit(1)

def get_valid_and_invalid_files(files):
    valid_files = []
    invalid_files = []

    for file in files:
        modified_file = change_extension(file)
        if os.path.exists(modified_file) and is_valid_pdf_file(modified_file):
            valid_files.append(modified_file)
        else:
            invalid_files.append(file)

    return valid_files, invalid_files

def get_valid_files_in_directory(directory):
    valid_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if is_valid_pdf_file(file_path):
                valid_files.append(file_path)

    return valid_files

def is_valid_pdf_file(file_path):
    if not file_path.lower().endswith('.pdf'):
        return False

    try:
        with open(file_path, 'rb') as f:
            first_bytes = f.read(5)
            if first_bytes != b'%PDF-':
                return False
            return True
    except Exception as e:
        return False

def merge_and_print_output(valid_files, pdf_merger, directory, echo=False):
    output_path = generate_file_name(directory)
    save_output(output_path, pdf_merger)
    if echo:
        click.echo(click.style(f'Successfully merged {len(valid_files)} PDF files into {output_path}', fg='green'))
    else:
        click.echo(click.style(f"Successfully merged: {', '.join(valid_files)} into {output_path}", fg='green'))

def generate_file_name(directory, default_name='merged'):
    current_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = f"{default_name}_{current_timestamp}.pdf"
    output_path = os.path.join(directory, output_filename)
    return output_path