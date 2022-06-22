# PaperCrawler

Crawler for AI paper, especially for NLP.

## Requirements

- [Scrapy](https://scrapy.org/)

## Usage

### Command line

```
$ scrapy crawl <conference_name>
```

### Conference names
| Conference/Journal      | Name |
| ----------- | ----------- |
| ALC Series    | `acls`    |
| TACL Series   | `tacl`    |
| ICLR          | `iclr`    |
| ICML          | `icml`    |
| NeurIPS       | `nips`    |

## Update

### 2022.6.22

Upload the crawlers of ACL Series (ACL, EMNLP, NAACL, COLING) and TACL Series (TACL, CL) from 2018 to 2022

Upload the crawlers of ICLR, ICML and NeurIPS from 2018 to 2021

## TODO

- [ ] Upload the crawlers of AAAI and IJCAI
- [ ] Splitting out individual conference crawlers from the ACL series and TACL series
- [ ] Add a year parameter to download conference papers for a particular year separately
