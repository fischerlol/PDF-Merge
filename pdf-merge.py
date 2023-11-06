from pdf_helpers import *

@click.command()
@click.option('-d', '--directory', type=click.Path(exists=True), default=None, help='Directory containing PDF files to merge.')
@click.option('-c', '--current', is_flag=True, help='Merge all PDFs in the current directory.')
@click.option('-f', '--file', multiple=True, type=str, help='PDF files to merge: -f 1 -f 2 -f 3 ...')
@click.option('-o', '--output', type=str, default='merged.pdf', help='Name of output file.')
def pdf_merge(directory, current, file, output):
    pdf_merger = PdfMerger()

    ensure_exclusivity(directory, current, file)

    if directory:
        merge_pdf_directory(directory, pdf_merger, output)
    elif file:
        merge_pdf_files(file, pdf_merger, output)
    elif current:
        merge_pdf_current_directory(pdf_merger, output)
    else:
        click.echo(click.style("pdf-merge: try 'pdf-merge --help' for more information", fg='yellow'))

def merge_pdf_directory(directory, pdf_merger, output):
    valid_files = get_valid_files_in_directory(directory)

    if not valid_files:
        click.echo(click.style(f'The directory: {directory} does not contain any valid .pdf files', fg='red'))
        sys.exit(1)

    progress_bar(valid_files, f'Merging {len(valid_files)} files from directory', pdf_merger)
    merge_and_print_output(valid_files, pdf_merger, directory, output)

def merge_pdf_files(files, pdf_merger, output):
    valid_files, invalid_files = get_valid_and_invalid_files(files)

    handle_invalid_files(invalid_files)

    progress_bar(valid_files, f'Merging {", ".join(valid_files)} :', pdf_merger)
    merge_and_print_output(valid_files, pdf_merger, os.getcwd(), output, True)

def merge_pdf_current_directory(pdf_merger, output):
    directory = os.getcwd()
    directory_listing = os.listdir(directory)

    valid_files, invalid_files = get_valid_and_invalid_files(directory_listing)

    if not valid_files:
        click.echo(click.style(f'The directory: {directory} does not contain any valid .pdf files', fg='red'))
        sys.exit(1)

    progress_bar(valid_files, f'Merging {len(valid_files)} files from {directory}', pdf_merger)
    merge_and_print_output(valid_files, pdf_merger, directory, output)

if __name__ == "__main__":
    pdf_merge()