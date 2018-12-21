# -*- coding: utf-8 -*-

"""Search Wikipedia articles."""

from albertv0 import *
import os

__iid__ = "PythonInterface/v0.2"
__prettyname__ = "Google Drive"
__version__ = "0.1"
__trigger__ = "drive "
__author__ = "Hugo Valk"
__dependencies__ = []

iconPath = iconLookup('gdrive')
if not iconPath:
    iconPath = os.path.dirname(__file__)+"/gdrive.png"
baseurl = 'https://drive.google.com'
user_agent = "org.albert.extension.python.gdrive"


def new_doc_item(trigger):
    item = Item(id=__prettyname__,
                icon=iconPath)
    item.text = "Create new document"
    item.completion = trigger + " doc"
    item.addAction(UrlAction('Create new doumentc', "docs.new"))
    return item


def new_sheet_item(trigger):
    item = Item(id=__prettyname__,
                icon=iconPath)
    item.text = "Create new spreadsheet"
    item.completion = trigger + " sheet"
    item.addAction(UrlAction('Create new spreadsheet', "sheets.new"))
    return item


def new_slides_item(trigger):
    item = Item(id=__prettyname__,
                icon=iconPath)
    item.text = "Create new presentation"
    item.completion = trigger + " slides"
    item.addAction(UrlAction('Create new presentation', "slides.new"))
    return item


def new_form_item(trigger):
    item = Item(id=__prettyname__,
                icon=iconPath)
    item.text = "Create new form"
    item.completion = trigger + " form"
    item.addAction(UrlAction('Create new Google form', "forms.new"))
    return item


def create_new(fields):
    trigger = __trigger__ + "new"
    items = [
        new_doc_item(trigger),
        new_sheet_item(trigger),
        new_slides_item(trigger),
        new_form_item(trigger)
    ]
    if len(fields) > 1:
        items = filter(lambda i: fields[1] in i.completion, items)
    return items


def handleQuery(query):
    if query.isTriggered:
        fields = query.string.split()
        if len(fields) >= 1 and fields[0] == 'new':
            return create_new(fields)
        else:
            item = Item(id=__prettyname__,
                        icon=iconPath)
            item.text = "Create new ..."
            item.completion = __trigger__ + "new"
            return item
