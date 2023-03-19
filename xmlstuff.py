# this imports the XML module as a shortened variable
import xml.etree.ElementTree as ET

# this is really just one big string named data
data = '''
<person>
    <name>Chuck</name>
    <phone type="intl">
        +1 734 303 4456
    </phone>
    <email hide="yes"/>
</person>'''

# define tree as "ET" function from the data string we made
# tree is no longer a string, but has turned the <> tags into python objects
tree = ET.fromstring(data)
# asks to find tag "name" and pull the text value from it
# the first argument after print is just printing text
print('Name:', tree.find('name').text)
# this one gets the value of the "hide" attribute
print('Attr:', tree.find('email').get('hide'))
