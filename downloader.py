from internetarchive import search_items, download
import argparse

def search_and_download_items(search_str, format_list):
    items = search_items(search_str)
    if len(items) == 0:
        print(f'The parameters of your search using search string: "{search_str}" found no results!')

    for item in items.iter_as_items():
        try:
            download(item.identifier, verbose=True, formats=format_list)
        except Exception as e:
            print("Skipping " + item.identifier + " due to an exception")
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--collection', type=str, default='')
    parser.add_argument('--year', type=str, default='')
    parser.add_argument('--year_range',type=str, default='',help='A range of years, must be in the format 1900-1999')
    parser.add_argument('--language', type=str, default='')
    parser.add_argument('--subject', type=str, default='')
    parser.add_argument('--identifier', type=str, default='')
    parser.add_argument('--creator', type=str, default='')
    parser.add_argument('--media_type', type=str, default='')
    parser.add_argument('--data_type', type=str, default='', choices=['image', 'text', 'audio', 'pdf'])
    parser.add_argument('--speciic_format', type=str, default='')
    parser.add_argument('--glob_pattern', type=str, default='', help='Search for a specific extension using a glob pattern, i.e.: "*.png"')

    args = parser.parse_args()

    search_str = ""
    format_list = []

    if args.collection != '':
        search_str += f'collection:{args.collection} '
    if args.year != '' and args.year_range == '':
        search_str += f'year:{args.year} '
    if args.language != '':
        search_str += f'language:{args.language} '
    if args.subject != '':
        search_str += f'subject:{args.subject} '
    if args.media_type != '':
        search_str += f'mediatype:{args.media_type} '
    if args.identifier != '':
        search_str += f'identifier:{args.identifier} '
    if args.creator != '':
        search_str += f'creator:{args.creator} '
    if args.glob_pattern != '':
        search_str += f'glob_pattern:{args.glob_pattern} '       

    if args.data_type == 'image':
        format_list.extend(['JPEG','PNG'])
    elif args.data_type == 'pdf':
        format_list.extend(['Image Container PDF','Text PDF'])
    elif args.data_type == 'text':
        format_list.append('FULL TEXT')
    elif args.data_type == 'audio':
        format_list.append('64KBPS MP3')

    if args.speciic_format != '':
        format_list.append(args.speciic_format)
    
    if args.year_range == '':
        search_and_download_items(search_str, format_list)
    else:
        start_year, end_year = args.year_range.split('-')
        for year in range(int(start_year),int(end_year)):
            s_str = search_str + f'year:{year} '
            search_and_download_items(s_str, format_list) 


