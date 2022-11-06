# pdf-scraper

Scrape data from PDF files using python.

## Usage

The `scripts` directory contains below scripts:

- `explore.py` - use this exploratory script to locate coordinates of text fields you are interested in.
- `script.py` - input coordinates from the explore script into this script and run to extract desired fields to an output file.

The `files` directory contains sample ADP format pay stub template (chosen as example of a consistent structure) PDF file to be scraped.

## Versioning

<https://semver.org>

Example

```bash
0.0.1
0.0.1-rc.1
```

## Local Development

```bash
make list    # list all container and images

make build   # build image

make start   # start container

make shell   # start shell in running container

make stop    # stop container

make remove  # remove container

make clean   # remove images
```

## References

<https://towardsdatascience.com/scrape-data-from-pdf-files-using-python-and-pdfquery-d033721c3b28>
