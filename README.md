# Internet archive downloader

 A set of Python3 scripts and utility functions for querying and downloading data from the [internet archive](http://archive.org) . 

## Installation instructions

Navigate to and follow the installation instructions for the internet archives python library: [https://archive.org/services/docs/api/internetarchive/installation.html](https://archive.org/services/docs/api/internetarchive/installation.html)

## Usage

### Querying the internet archive

Use search.py to query the internet archive to see the total number of results found for specified search parameters:

    python3 search.py --collection=metropolitanmuseumofart-gallery --subject=etching

You can specify individual years with the `--year` flag or a range of dates with the `--year_range` flag, note the date range must be in the format YYYY-YYYY:

   

    python3 search.py --collection=metropolitanmuseumofart-gallery --subject=etching --year_range=1800-1899

Use the flag `--verbose` to list all of the individual search results.

### Downloading from the internet archive

Once you have found a set of search parameters that give you a a set of results, you can use the downloader.py script to download all the results for a given search.

You will likely want to specify a specific format or file type type for downloading. There are three ways of doing this.

Specifying a preset data type with the flag `--data_type`:

`python3 downloader.py --collection=metropolitanmuseumofart-gallery --subject=etching --data_type=image`

Specify a specific format as listed by the internet archive database:

`python3 downloader.py --collection=metropolitanmuseumofart-gallery --subject=etching --specific_format=JPEG`

Use a glob pattern to search for a specific file extension:

`python3 downloader.py --collection=metropolitanmuseumofart-gallery --subject=etching --glob_pattern=*.jpg`