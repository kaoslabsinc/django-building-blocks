from building_blocks.admin.utils import render_element, json_field_pp


def test_json_field_pp_unsafe():
    d = {'field': "<script>malicious_code()</script>"}
    html = json_field_pp(d)
    assert '&lt;script&gt;' in html


def test_render_element():
    assert render_element('br') == '''<br >'''
    assert render_element('img', attrs={'src': "img.png"}) == '''<img src="img.png">'''
    assert render_element('p', "Content") == '''<p >Content</p>'''
    assert render_element('p', "Content", attrs={'class': "text-bold"}) == '''<p class="text-bold">Content</p>'''


def test_render_element_unsafe_children():
    el = render_element('p', "<script>malicious_code()</script>")
    assert el != '''<p ><script>malicious_code()</script></p>'''


def test_render_element_unsafe_attrs():
    el = render_element('p', children="", attrs={'class': '''"/><script>malicious_code()</script>'''})
    assert el != '''<p class=""/><script>malicious_code()</script>"></p>'''
    assert '&quot;' in el
    assert '&lt;script&gt;' in el
