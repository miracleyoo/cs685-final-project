import json
import time
from urllib import request

def crawl_one(url):
    try:
        res = str(request.urlopen(url).read(), 'utf-8')
    except Exception as e:
        with open('log.txt', 'a+') as f:
            print(f'[ERROR]: {str(e)}')
            f.writelines(str(e)+f': {url}\n')
        time.sleep(360)
        res = crawl_one(url)
    return res

def get_paper_info(paper, fos=None):
    paper_id = paper['paperId']
    # Each paper info pack consists title, abstract, authors, tldr, citation count, field of study
    paper_url = f'https://api.semanticscholar.org/graph/v1/paper/{paper_id}?fields=title,abstract,citations.authors,tldr,citationCount,influentialCitationCount,fieldsOfStudy'
    paper_info = crawl_one(paper_url)
    paper_info = json.loads(paper_info)
    # Filter out the papers out of field of study
    if (fos is not None and paper_info['fieldsOfStudy'] is not None and fos not in paper_info['fieldsOfStudy']) or paper_info['tldr'] is None:
        return
    return paper_info



# def get_paper_info(paper, fos=None):
#     try:
#         paper_id = paper['paperId']
#         # Each paper info pack consists title, abstract, authors, tldr, citation count, field of study
#         paper_url = f'https://api.semanticscholar.org/graph/v1/paper/{paper_id}?fields=title,abstract,citations.authors,tldr,citationCount,influentialCitationCount,fieldsOfStudy'
#         paper_info = str(request.urlopen(paper_url).read(), 'utf-8')
#         paper_info = json.loads(paper_info)
#         # Filter out the papers out of field of study
#         if (fos is not None and fos not in paper_info['fieldsOfStudy']) or paper_info['tldr'] is None:
#             return
#         return paper_info
#     except Exception as e:
#         with open('log.txt', 'a+') as f:
#             f.writelines(str(e))
#             f.writelines('\n')
#         return

    # tldr = paper_info['tldr']
    # if tldr is not None:
    #     tldr_cat += ' '+tldr['text'].strip()
    #     info_pack.append(paper_info)