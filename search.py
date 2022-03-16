from internetarchive import search_items, download
import argparse

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
    parser.add_argument('--verbose', type=bool, default=False)

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
    if args.identifier != '':
        search_str += f'identifier:{args.identifier} '
    if args.creator != '':
        search_str += f'creator:{args.creator} '   
    if args.media_type != '':
        search_str += f'mediatype:{args.media_type} '
    
    item_list = []
    if args.year_range == '':
        item_list = search_items(search_str)
    else:
        start_year, end_year = args.year_range.split('-')
        for year in range(int(start_year),int(end_year)):
            s_str = search_str + f'year:{year} '
            year_list = search_items(s_str)
            item_list.extend(year_list)
            print(f'For the year {year}: {len(year_list)} items were found.')
    
    print(f'In total {len(item_list)} items were found for your search.')
    if(args.verbose == True):
        for item in item_list.iter_as_items():
            print(item.identifier)


