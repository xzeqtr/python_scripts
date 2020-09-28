from tika import parser
import re
file = ('GTD.pdf')
raw_xml = parser.from_file(file, xmlContent=True)
body = raw_xml['content'].split('<body>')[1].split('</body>')[0]
body_without_tag = body.replace("<p>", "").replace(
    "</p>", "").replace("<div>", "").replace("</div>", "").replace("<p />", "")
text_pages = body_without_tag.split("""<div class="page">""")[1:]
num_pages = len(text_pages)

first_page = body.split("""<div class="page">""")[1:][0]
awb = re.findall('02017/0 (.*)\n', first_page)[0]
awb_num, awb_date = awb.split(' ОТ ')
