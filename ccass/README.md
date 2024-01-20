# CCASS Search

You can search and compare two dates of CCASS shareholding information from HKEX source.

## How is work

### For python script file - ccass_search.py

```console
> python ccass_search.py -h

usage: ccass_search.py [-h] -c CODE -s START -e END [--lang {e,c}] [--sort {id,name,start,end,change,change-percent}]

You can search and compare two dates of CCASS shareholding information from HKEX source.

example: python ccass_search.py -c 941 -s 2023/10/01 -e 2024/01/02 --lang c --sort change

Please provide following informaiton:
------------------------------------------------------------------------------------------------------------
-c CODE               Stock Code (example: 1)
-s START              Shareholding Start Date (example: 2024/12/30)
-e END                Shareholding End Date (example: 2024/12/31)
--lang                Display Language (default: c)
                      Options:
                        e: English
                        c: Chinese
--sort                Sort by value (default: change)
                      Options:
                        id: Participant Id
                        name: Participant Name
                        start: Shareholding Start
                        end: Shareholding End
                        change: Shareholding Change
                        change-percent: Shareholding Change Percent
------------------------------------------------------------------------------------------------------------

options:
  -h, --help            show this help message and exit
  -c CODE
  -s START
  -e END
  --lang {e,c}
  --sort {id,name,start,end,change,change-percent}

License
------------------------------------------------------------------------------------------------------------
MIT - a permissive free software license originating at the Massachusetts
Institute of Technology (MIT), it puts only very limited restriction on
reuse and has, therefore, an excellent license compatibility. It permits
reuse within proprietary software provided that all copies of the licensed
software include a copy of the MIT License terms and the copyright notice.

Check the LICENSE file (https://github.com/jasonlws/hkex-tools/blob/main/LICENSE) for more details.
```

```console
> python ccass_search.py -c 941 -s 2023/10/01 -e 2024/01/02 --lang c --sort change

                                                                2023/10/01             2024/01/02            持股量 (%)
B01161 - UBS SECURITIES HONG KONG LTD                  149,172,770 (0.69%)    167,934,465 (0.78%)   18,761,695 (12.58%)
C00093 - 法國巴黎銀行                                    49,177,727 (0.22%)     63,289,038 (0.29%)   14,111,311 (28.69%)
C00111 - Societe Generale                                8,512,213 (0.03%)     14,915,796 (0.06%)    6,403,583 (75.23%)
B01228 - 中信証券經紀(香港)有限公司                       19,002,782 (0.08%)     24,706,458 (0.11%)    5,703,676 (30.01%)
B01555 - ABN AMRO CLEARING HONG KONG LTD                 1,013,814 (0.00%)      6,298,692 (0.02%)   5,284,878 (521.29%)
B01224 - MLFE LTD                                        8,802,024 (0.04%)     13,220,928 (0.06%)    4,418,904 (50.20%)
C00042 - 招商永隆銀行有限公司                             29,107,649 (0.13%)     32,203,470 (0.15%)    3,095,821 (10.64%)
B01832 - 瑞穗證券亞洲有限公司                                 39,000 (0.00%)      2,772,000 (0.01%)  2,733,000 (7007.69%)
B01451 - 高盛(亞洲)證券有限公司                           29,023,497 (0.13%)     31,034,392 (0.14%)     2,010,895 (6.93%)
B01727 - 工銀亞洲証券有限公司                             19,405,821 (0.09%)     21,326,620 (0.09%)     1,920,799 (9.90%)
C00041 - 華僑銀行(香港)有限公司                           16,267,737 (0.07%)     17,884,770 (0.08%)     1,617,033 (9.94%)
...                                                                  ...                     ...                   ...
B01491 - CREDIT SUISSE SECURITIES (HONG KONG) LTD          642,393 (0.00%)         10,210 (0.00%)    -632,183 (-98.41%)
C00003 - 東亞銀行有限公司                                21,825,486 (0.10%)     21,153,269 (0.09%)     -672,217 (-3.08%)
B01274 - MORGAN STANLEY HONG KONG SECURITIES LTD        28,855,058 (0.13%)     27,987,132 (0.13%)     -867,926 (-3.01%)
C00040 - 中國工商銀行(亞洲)有限公司                       63,765,459 (0.29%)     62,861,759 (0.29%)     -903,700 (-1.42%)
B01376 - 大眾証券有限公司                                   960,000 (0.00%)              0 (0.00%)   -960,000 (-100.00%)
C00018 - 恒生銀行有限公司                                76,919,203 (0.35%)     75,918,083 (0.35%)   -1,001,120 (-1.30%)
B01654 - 中國國際金融香港證券有限公司                     10,146,260 (0.04%)      9,005,160 (0.04%)  -1,141,100 (-11.25%)
B01668 - 耀才證券國際(香港)有限公司                       13,128,075 (0.06%)     11,960,075 (0.05%)   -1,168,000 (-8.90%)
C00016 - DBS BANK LTD                                   44,572,224 (0.20%)     41,720,979 (0.19%)   -2,851,245 (-6.40%)
C00039 - 渣打銀行(香港)有限公司                         337,360,085 (1.57%)    332,974,381 (1.55%)   -4,385,704 (-1.30%)
C00100 - JPMORGAN CHASE BANK, NATIONAL ASSOCIATION    110,514,231 (0.51%)    104,856,184 (0.49%)   -5,658,047 (-5.12%)
C00010 - 花旗銀行                                      218,960,269 (1.02%)    212,930,992 (0.99%)   -6,029,277 (-2.75%)
A00003 - 中國証券登記結算有限責任公司                  1,271,368,213 (5.94%)  1,264,178,029 (5.91%)   -7,190,184 (-0.57%)
C00019 - 香港上海匯豐銀行有限公司                        936,705,108 (4.38%)    915,480,234 (4.28%)  -21,224,874 (-2.27%)
A00004 - CHINA SECURITIES DEPOSITORY AND CLEARING     984,757,499 (4.60%)    958,492,679 (4.48%)  -26,264,820 (-2.67%)
```

Alternative, you can use the Jupyter Notebook - [ccass_search.ipynb](ccass_search.ipynb).

## Reference Links

- https://www3.hkexnews.hk/sdw/search/searchsdw.aspx
- https://www3.hkexnews.hk/sdw/search/searchsdw_c.aspx

## License

MIT - a permissive free software license originating at the Massachusetts Institute of Technology (MIT), it puts only very limited restriction on reuse and has, therefore, an excellent license compatibility. It permits reuse within proprietary software provided that all copies of the licensed software include a copy of the MIT License terms and the copyright notice.

Check the [LICENSE file](../LICENSE) for more details.