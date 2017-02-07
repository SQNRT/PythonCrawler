# coding = utf8
'''
Created on 2017/2/4

@author: fxyoy
'''
import urllib.request





class HtmlDownloader(object):
    
    
    def download(self, url):
        if url is None:
            return None
        response = urllib.request.urlopen(url)
        if response.getcode() != 200:
            return None
        return response.read()
    
    



