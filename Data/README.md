# *Craw recruit data on TOPCV*

## Requirements:
- requests
- BeautifulSoup4

## Crawl data on [TOPCV](https://www.topcv.vn/tim-viec-lam-it-phan-mem-c10026?salary=0&exp=0&company_field=0&sort=up_top&page=)
- Open folder withterminal, type `py crawl_data.py x y` <br>
(`x`, `y` are the index of begin and end of webpage want to crawl)
- This command will crawl data from consecutive webpages from page `x` to page `y`

## Default Run
- bash crawl.sh to crawl all data on first 170 page. Then, we have 17 files .json store data.

