import os
import random

import genanki


def create_apkg(name,l):
    # MODELID = random.randrange(1 << 30, 1 << 31)
    MODELID = 1382232460
    my_model = genanki.Model(
        MODELID,
        "Example",
        fields=[
            {"name": "Question"},
            {"name": "Answer"},
            
            {'name': 'Code'},
            {'name': 'Reference'},
            {'name': 'Example'},
            {'name': 'Add Reverse'},
        ],
        templates=[
            {
                "name": "Front_Back",
                "qfmt": "{{Question}}",
                "afmt": '''{{FrontSide}}<hr id=answer>{{Answer}}<br><br>
                           <br>{{#Code}}<u>Code:</u>{{Code}}{{/Code}}<br>
                           <br>{{#Reference}}<u>Reference:</u>{{Reference}}{{/Reference}}<br>
                           <br>{{#Example}}<u>Example:</u>  {{Example}}{{/Example}}<br>
                        ''',
            },
            {
                'name': 'Back_Front',
                'qfmt': '{{#Add Reverse}}{{Answer}}{{/Add Reverse}}',
                'afmt': """{{FrontSide}}<hr id=answer>{{Question}}<br><br>
                           <br>{{#Code}}<u>Code:</u>{{Code}}{{/Code}}<br>
                           <br>{{#Reference}}<u>Reference:</u>{{Reference}}{{/Reference}}<br>
                           <br>{{#Example}}<u>Example:</u>  {{Example}}{{/Example}}<br>
                       """,
            




            },
        ],
        
    )
    # deckId = random.randrange(1 << 30, 1 << 31)
    deckId = 1382232460
    my_deck = genanki.Deck(deckId, name)
    DIRECTORY = "Temp"
    count = 0
    filelist = sorted(os.listdir(DIRECTORY))
    filelist.remove("input.pdf")
    # print(filelist)
    # print("filelist " + str(len(filelist)))
    while count < len(l):
        # field1 = r'<img src="%s"\>' % (filelist[count])
        # field2 = r'<img src="%s"\>' % (filelist[count + 1])
        field1 = r'<img src="%s"\>' % (l[count])
        field2 = r'<img src="%s"\>' % (l[count+1])
        field3=''
        field4=''
        field5=''
        field6=''
        my_note = genanki.Note(model=my_model, fields=[field1, field2,field3,field4,field5,field6])
        my_deck.add_note(my_note)
        count = count + 2
    my_package = genanki.Package(my_deck)
    for x in filelist:
        my_package.media_files.append("Temp" + os.sep + x)
    my_package.write_to_file("%s.apkg" % name)
