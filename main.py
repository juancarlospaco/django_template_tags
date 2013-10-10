# -*- coding: utf-8 -*-
# PEP8:NO, LINT:OK, PY3:NO


#############################################################################
## This file may be used under the terms of the GNU General Public
## License version 2.0 or 3.0 as published by the Free Software Foundation
## and appearing in the file LICENSE.GPL included in the packaging of
## this file.  Please review the following information to ensure GNU
## General Public Licensing requirements will be met:
## http:#www.fsf.org/licensing/licenses/info/GPLv2.html and
## http:#www.gnu.org/copyleft/gpl.html.
##
## This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
## WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.
#############################################################################


# metadata
" Ninja Django Template Tags "
__version__ = ' 0.2 '
__license__ = ' GPL '
__author__ = ' juancarlospaco '
__email__ = ' juancarlospaco@ubuntu.com '
__url__ = ''
__date__ = ' 20/10/2013 '
__prj__ = ' '
__docformat__ = 'django_template_tags'
__source__ = ''
__full_licence__ = ''


# imports
from os import path
from datetime import datetime
from getpass import getuser
from PyQt4.QtGui import (QMenu, QInputDialog, QDialog, QGroupBox, QPushButton,
    QTextEdit, QColor, QVBoxLayout, QLabel, QGraphicsDropShadowEffect,
    QApplication, QAction, QFileDialog)

from ninja_ide.core import plugin


###############################################################################


class Main(plugin.Plugin):
    " Main Class "
    def initialize(self, *args, **kwargs):
        " Init Main Class "
        super(Main, self).initialize(*args, **kwargs)
        self.locator.get_service("menuApp").add_action(QAction(' ', self))
        # Django Builtin Template Tags
        self.menu0 = QMenu("Django Template TAGS")
        self.menu0a = QMenu("Boolean Operators")
        self.menu0.addAction('autoescape - Auto Escape characters', lambda: self.templatag('autoescape'))
        self.menu0.addSeparator()
        self.menu0.addAction('block - Named Block to override by child template', lambda: self.templatag('block'))
        self.menu0.addSeparator()
        self.menu0.addAction('comment - Multiline Comments', lambda: self.templatag('comment'))
        self.menu0.addAction('csrf_token - Cross Site Request Forgery Token', lambda: self.templatag('csrf_token'))
        self.menu0.addAction('cycle - Cycle variables each time its used', lambda: self.templatag('cycle'))
        self.menu0.addSeparator()
        self.menu0.addAction('debug - Builtin Debug info with Context and Modules', lambda: self.templatag('debug'))
        self.menu0.addSeparator()
        self.menu0.addAction('extends - Extends a parent template', lambda: self.templatag('extends'))
        self.menu0.addAction('extends - Extends a parent template with Open File Dialog', lambda: self.templatag('extendsfile'))
        self.menu0.addSeparator()
        self.menu0.addAction('filter - Filtered Block for one or more filters', lambda: self.templatag('filter'))
        self.menu0.addAction('firstof - Outputs first argument variable that is True', lambda: self.templatag('firstof'))
        self.menu0.addAction('for - For Loop', lambda: self.templatag('for'))
        self.menu0.addAction('for...empty - For Loop with Fallback if Empty loop', lambda: self.templatag('for...empty'))
        self.menu0.addSeparator()
        self.menu0.addAction('if - If Conditional', lambda: self.templatag('if'))
        self.menu0.addAction('ifchanged - Check if value changed from last loop iteration', lambda: self.templatag('ifchanged'))
        self.menu0.addAction('ifequal - Output block contents if 2 arguments equal each other', lambda: self.templatag('ifequal'))
        self.menu0.addAction('ifnotequal - Output block contents if 2 arguments Not equal each other', lambda: self.templatag('ifnotequal'))
        self.menu0.addAction('include - Load and render template with current context', lambda: self.templatag('include'))
        self.menu0.addAction('include - Render template with current context with Open File Dialog', lambda: self.templatag('includefile'))
        self.menu0.addSeparator()
        self.menu0.addAction('load - Loads a custom template tag', lambda: self.templatag('load'))
        self.menu0.addSeparator()
        self.menu0.addAction('now - Display current date and time', lambda: self.templatag('now'))
        self.menu0.addSeparator()
        self.menu0.addAction('regroup - Regroup list of alike objects by common attribute', lambda: self.templatag('regroup'))
        self.menu0.addSeparator()
        self.menu0.addAction('spaceless - Removes whitespace between HTML tags', lambda: self.templatag('spaceless'))
        self.menu0.addAction('ssi - Output contents of a given file into the page', lambda: self.templatag('ssi'))
        self.menu0.addAction('ssi - Output content of file into the page with Open File Dialog', lambda: self.templatag('ssifile'))
        self.menu0.addAction('templatetag - Output syntax characters used for template tags', lambda: self.templatag('templatetag'))
        self.menu0.addSeparator()
        self.menu0.addAction('verbatim - Stops template engine from rendering contents of the block', lambda: self.templatag('verbatim'))
        self.menu0.addSeparator()
        self.menu0.addMenu(self.menu0a)
        self.menu0a.addAction('== operator', lambda: self.templatag('== operator'))
        self.menu0a.addAction('!= operator', lambda: self.templatag('!= operator'))
        self.menu0a.addAction('< operator', lambda: self.templatag('< operator'))
        self.menu0a.addAction('> operator', lambda: self.templatag('> operator'))
        self.menu0a.addAction('<= operator', lambda: self.templatag('<= operator'))
        self.menu0a.addAction('>= operator', lambda: self.templatag('>= operator'))
        self.menu0a.addSeparator()
        self.menu0a.addAction('in operator - A in B comparation', lambda: self.templatag('in operator'))
        self.menu0a.addAction('not in operator - A not in B comparation', lambda: self.templatag('not in operator'))
        self.locator.get_service("menuApp").add_menu(self.menu0)

        # Django Builtin Template Filters
        self.menu1 = QMenu("Django Template FILTERS")
        self.menu1.addAction('add', lambda: self.templatag('add'))
        self.menu1.addAction('addslashes', lambda: self.templatag('addslashes'))
        self.menu1.addSeparator()
        self.menu1.addAction('center', lambda: self.templatag('center'))
        self.menu1.addAction('cut', lambda: self.templatag('cut'))
        self.menu1.addSeparator()
        self.menu1.addAction('date', lambda: self.templatag('date'))
        self.menu1.addAction('default', lambda: self.templatag('default'))
        self.menu1.addAction('default_if_none', lambda: self.templatag('default_if_none'))
        self.menu1.addAction('dictsort', lambda: self.templatag('dictsort'))
        self.menu1.addAction('dictsortreversed', lambda: self.templatag('dictsortreversed'))
        self.menu1.addAction('divisibleby', lambda: self.templatag('divisibleby'))
        self.menu1.addSeparator()
        self.menu1.addAction('escape', lambda: self.templatag('escape'))
        self.menu1.addAction('escapejs', lambda: self.templatag('escapejs'))
        self.menu1.addSeparator()
        self.menu1.addAction('filesizeformat', lambda: self.templatag('filesizeformat'))
        self.menu1.addAction('first', lambda: self.templatag('first'))
        self.menu1.addAction('fix_ampersands', lambda: self.templatag('fix_ampersands'))
        self.menu1.addAction('floatformat', lambda: self.templatag('floatformat'))
        self.menu1.addAction('force_escape', lambda: self.templatag('force_escape'))
        self.menu1.addSeparator()
        self.menu1.addAction('get_digit', lambda: self.templatag('get_digit'))
        self.menu1.addSeparator()
        self.menu1.addAction('iriencode', lambda: self.templatag('iriencode'))
        self.menu1.addSeparator()
        self.menu1.addAction('join', lambda: self.templatag('join'))
        self.menu1.addSeparator()
        self.menu1.addAction('last', lambda: self.templatag('last'))
        self.menu1.addAction('lenght', lambda: self.templatag('lenght'))
        self.menu1.addAction('lenght_is', lambda: self.templatag('lenght_is'))
        self.menu1.addAction('linebreaks', lambda: self.templatag('linebreaks'))
        self.menu1.addAction('linebreaksbr', lambda: self.templatag('linebreakesbr'))
        self.menu1.addAction('linenumbers', lambda: self.templatag('linenumbers'))
        self.menu1.addAction('ljust', lambda: self.templatag('ljust'))
        self.menu1.addAction('lower', lambda: self.templatag('lower'))
        self.menu1.addSeparator()
        self.menu1.addAction('make_list', lambda: self.templatag('make_list'))
        self.menu1.addSeparator()
        self.menu1.addAction('phone2numeric', lambda: self.templatag('phone2numeric'))
        self.menu1.addAction('pluralize', lambda: self.templatag('pluralize'))
        self.menu1.addSeparator()
        self.menu1.addAction('random', lambda: self.templatag('random'))
        self.menu1.addSeparator()
        self.menu1.addAction('pprint', lambda: self.templatag('pprint'))
        self.menu1.addSeparator()
        self.menu1.addAction('removetags', lambda: self.templatag('removetags'))
        self.menu1.addAction('rjust', lambda: self.templatag('rjust'))
        self.menu1.addSeparator()
        self.menu1.addAction('safe', lambda: self.templatag('safe'))
        self.menu1.addAction('safeseq', lambda: self.templatag('safeseq'))
        self.menu1.addAction('slice', lambda: self.templatag('slice'))
        self.menu1.addAction('slugify', lambda: self.templatag('slugify'))
        self.menu1.addAction('stringformat', lambda: self.templatag('stringformat'))
        self.menu1.addAction('striptags', lambda: self.templatag('striptags'))
        self.menu1.addSeparator()
        self.menu1.addAction('time', lambda: self.templatag('time'))
        self.menu1.addAction('timesince', lambda: self.templatag('timesince'))
        self.menu1.addAction('timeuntil', lambda: self.templatag('timeuntil'))
        self.menu1.addAction('title', lambda: self.templatag('title'))
        self.menu1.addAction('truncatechars', lambda: self.templatag('truncatechars'))
        self.menu1.addAction('truncatewords', lambda: self.templatag('truncatewords'))
        self.menu1.addAction('truncatewords_html', lambda: self.templatag('truncatewords_html'))
        self.menu1.addSeparator()
        self.menu1.addAction('unordered_list', lambda: self.templatag('unordered_list'))
        self.menu1.addAction('upper', lambda: self.templatag('upper'))
        self.menu1.addAction('urlencode', lambda: self.templatag('urlencode'))
        self.menu1.addAction('urlize', lambda: self.templatag('urlize'))
        self.menu1.addAction('urlizetrunc', lambda: self.templatag('urlizetrunc'))
        self.menu1.addSeparator()
        self.menu1.addAction('wordcount', lambda: self.templatag('wordcount'))
        self.menu1.addAction('wordwrap', lambda: self.templatag('wordwrap'))
        self.menu1.addSeparator()
        self.menu1.addAction('yesno', lambda: self.templatag('yesno'))
        self.locator.get_service("menuApp").add_menu(self.menu1)

        # Django Builtin Template Internacionalization
        #self.menu2 = QMenu("Django Template INTERNACIONALIZATION")
        #self.menu2.addAction('i18n', lambda: self.templatag('i18n'))
        #self.menu2.addSeparator()
        #self.menu2.addAction('l10n', lambda: self.templatag('l10n'))
        #self.menu2.addSeparator()
        #self.menu2.addAction('tz', lambda: self.templatag('tz'))
        #self.menu2.addSeparator()
        #self.locator.get_service("menuApp").add_menu(self.menu2)

        # Django Builtin Template Humanize
        self.menu3 = QMenu("Django Template HUMANIZE")
        self.menu3.addAction('apnumber - Numbers 1~9 as Words, >=10 as Integers', lambda: self.templatag('apnumber'))
        self.menu3.addSeparator()
        self.menu3.addAction('intcomma - Integers to Strings with Thousand commas', lambda: self.templatag('intcomma'))
        self.menu3.addAction('intword - Big Integers to Human String representation', lambda: self.templatag('intword'))
        self.menu3.addSeparator()
        self.menu3.addAction('naturalday - Date to yesterday,today,tomorrow else Date', lambda: self.templatag('naturalday'))
        self.menu3.addAction('naturaltime - Date Time to Human String representation', lambda: self.templatag('naturaltime'))
        self.menu3.addSeparator()
        self.menu3.addAction('ordinal - Integer to Ordinal String', lambda: self.templatag('ordinal'))
        self.menu3.addSeparator()
        self.locator.get_service("menuApp").add_menu(self.menu3)

        # Django Builtin Template Web Design
        self.menu4 = QMenu("Django Template WEB DESIGN")
        self.menu4.addAction('lorem - Builtin Lorem Impsum Generator', lambda: self.templatag('lorem'))
        self.locator.get_service("menuApp").add_menu(self.menu4)

        # Django Builtin Template Static
        self.menu5 = QMenu("Django Template STATIC")
        self.menu5.addAction('static - Add static file from path string', lambda: self.templatag('static'))
        self.menu5.addAction('static - Add static file with Open File Dialog', lambda: self.templatag('staticfile'))
        self.menu5.addSeparator()
        self.menu5.addAction('get_static_prefix - Output static prefix', lambda: self.templatag('get_static_prefix'))
        self.menu5.addAction('get_media_prefix  - Output media prefix', lambda: self.templatag('get_media_prefix'))
        self.locator.get_service("menuApp").add_menu(self.menu5)

        # Django comments
        self.menu6 = QMenu("Django Template COMMENTS")
        self.menu6.addAction('Single Line Comment from Selected Text', lambda: self.templatag('singlelinecomment'))
        self.menu6.addAction('Multi Line Comment from Selected Text', lambda: self.templatag('multilinecomment'))
        self.menu6.addSeparator()
        self.menu6.addAction('Single Line Comment from Input PopUp', lambda: self.templatag('singlelinecommentpopup'))
        self.menu6.addAction('Multi Line Comment from Input PopUp', lambda: self.templatag('multilinecommentpopup'))
        self.menu6.addSeparator()
        self.menu6.addAction('Single Line Comment from Clipboard', lambda: self.templatag('singlelinecommentclipboard'))
        self.menu6.addAction('Multi Line Comment from Clipboard', lambda: self.templatag('multilinecommentclipboard'))
        self.menu6.addSeparator()
        self.menu6.addAction('Multi Line Comment from File', lambda: self.templatag('multilinecommentfile'))
        self.menu6.addAction('Single Line Comment from Date Time Now', lambda: self.templatag('singlelinecommentdatetime'))
        self.locator.get_service("menuApp").add_menu(self.menu6)

        # Django Third Party Popular Template Tags and Filters
        self.menu7 = QMenu("Django Template 3Party Tags")
        self.menu7.addAction('Im a Placeholder :)')
        self.locator.get_service("menuApp").add_menu(self.menu7)
        self.locator.get_service("menuApp").add_action(QAction(' ', self))

    def templatag(self, action):
        ' parse and generate template markup '
        # QMessageBox.information(None, __doc__, action)
        if action in 'autoescape':
            self.locator.get_service("editor").insert_text('{% autoescape on %} ' + str(self.locator.get_service("editor").get_actual_tab().textCursor().selectedText().encode("utf-8")) + ' {% endautoescape %}')
        elif action in 'block':
            self.locator.get_service("editor").insert_text('{% block ' + str(QInputDialog.getText(None, __doc__, "Type Block Name:", text='block_name')[0]).strip() + ' %} ' + str(self.locator.get_service("editor").get_actual_tab().textCursor().selectedText().encode("utf-8")) + ' {% endblock %}')
        elif action in 'comment':
            self.locator.get_service("editor").insert_text('{% comment %} ' + str(self.locator.get_service("editor").get_actual_tab().textCursor().selectedText().encode("utf-8")) + ' {% endcomment %}')
        elif action in 'csrf_token':
            self.locator.get_service("editor").insert_text('{% csrf_token %}')
        elif action in 'cycle':
            self.locator.get_service("editor").insert_text('{% cycle ' + str(QInputDialog.getText(None, __doc__, "Items to Cycle, Space separated:", text='item1 item2 item3')[0]).strip() + ' %} ')
        elif action in 'debug':
            self.locator.get_service("editor").insert_text('{% debug %}')
        elif action in 'extends':
            self.locator.get_service("editor").insert_text('{% extends "' + str(QInputDialog.getText(None, __doc__, "Parent Template to Extend:", text='base.html')[0]).strip() + '" %} ')
        elif action in 'extendsfile':
            self.locator.get_service("editor").insert_text('{% extends "' + str(path.abspath(QFileDialog.getOpenFileName(None, "{} - Open File".format(__doc__), path.expanduser("~"), '*.*(*.*)'))).strip() + '" %} ')
        elif action in 'filter':
            self.locator.get_service("editor").insert_text('{% filter ' + str(QInputDialog.getText(None, __doc__, "Multiple filters with arguments, pipes separated:", text='lower|safe')[0]).strip() + ' %} ' + str(self.locator.get_service("editor").get_actual_tab().textCursor().selectedText().encode("utf-8")) + ' {% endfilter %}')
        elif action in 'firstof':
            self.locator.get_service("editor").insert_text('{% filter force_escape %}{% firstof ' + str(QInputDialog.getText(None, __doc__, "Multiple variables, space separated:", text='var1 var2')[0]).strip() + ' "' + str(QInputDialog.getText(None, __doc__, "Literal string Fallback Value:", text='fallback_value')[0]).strip() + '" %} ' + str(self.locator.get_service("editor").get_actual_tab().textCursor().selectedText().encode("utf-8")) + ' {% endfilter %}')
        elif action in 'for':
            self.locator.get_service("editor").insert_text('{% for ' + str(QInputDialog.getText(None, __doc__, "Variable to use to Iterate:", text='item')[0]).strip() + ' in ' + str(QInputDialog.getText(None, __doc__, "Sequence to Iterate:", text='values')[0]).strip() + ' %} ' + str(self.locator.get_service("editor").get_actual_tab().textCursor().selectedText().encode("utf-8")) + ' {% endfor %}')
        elif action in 'for...empty':
            self.locator.get_service("editor").insert_text('{% if ' + str(QInputDialog.getText(None, __doc__, "String to check:", text='"foo"')[0]).strip() + ' %} ' + str(self.locator.get_service("editor").get_actual_tab().textCursor().selectedText().encode("utf-8")) + ' {% empty %} ' + str(QInputDialog.getText(None, __doc__, "Output to use if for loop is Empty:", text='"Nothing."')[0]).strip() + ' {% endfor %}')
        elif action in 'if':
            pass
        elif action in '== operator':
            pass
        elif action in '!= operator':
            pass
        elif action in '< operator':
            pass
        elif action in '> operator':
            pass
        elif action in '<= operator':
            pass
        elif action in '>= operator':
            pass
        elif action in 'in operator':
            self.locator.get_service("editor").insert_text('{% if ' + '{} in {}'.format(str(QInputDialog.getText(None, __doc__, "String to check:", text='"foo"')[0]).strip(), str(QInputDialog.getText(None, __doc__, "Variable to check into:", text='bar')[0]).strip()) + ' %} ' + str(self.locator.get_service("editor").get_actual_tab().textCursor().selectedText().encode("utf-8")) + ' {% endif %}')
        elif action in 'not in operator':
            self.locator.get_service("editor").insert_text('{% if ' + '{} not in {}'.format(str(QInputDialog.getText(None, __doc__, "String to check:", text='"foo"')[0]).strip(), str(QInputDialog.getText(None, __doc__, "Variable to check into:", text='bar')[0]).strip()) + ' %} ' + str(self.locator.get_service("editor").get_actual_tab().textCursor().selectedText().encode("utf-8")) + ' {% endif %}')
        elif action in 'ifchanged':
            self.locator.get_service("editor").insert_text('{% ifchanged ' + str(QInputDialog.getText(None, __doc__, "None, One or Multiple Variables to check if they changed, space separated:")[0]).strip() + ' %} ' + str(self.locator.get_service("editor").get_actual_tab().textCursor().selectedText().encode("utf-8")) + ' {% endifchanged %}')
        elif action in 'ifequal':
            self.locator.get_service("editor").insert_text('{% ifequal ' + str(QInputDialog.getText(None, __doc__, "2 Variables or Strings to compare if equal, space separated:", text='"foo" "foo"')[0]).strip() + ' %} ' + str(self.locator.get_service("editor").get_actual_tab().textCursor().selectedText().encode("utf-8")) + ' {% endifequal %}')
        elif action in 'ifnotequal':
            self.locator.get_service("editor").insert_text('{% ifnotequal ' + str(QInputDialog.getText(None, __doc__, "2 Variables or Strings to compare if Not equal, space separated:", text='"foo" "bar"')[0]).strip() + ' %} ' + str(self.locator.get_service("editor").get_actual_tab().textCursor().selectedText().encode("utf-8")) + ' {% endifnotequal %}')
        elif action in 'include':
            self.locator.get_service("editor").insert_text('{% include "' + str(QInputDialog.getText(None, __doc__, "Parent Template to Include:", text='footer.html')[0]).strip() + '" %} ')
        elif action in 'includefile':
            self.locator.get_service("editor").insert_text('{% include "' + str(path.abspath(QFileDialog.getOpenFileName(None, "{} - Open File".format(__doc__), path.expanduser("~"), '*.*(*.*)'))).strip() + '" %} ')
        elif action in 'load':
            self.locator.get_service("editor").insert_text('{% load ' + str(QInputDialog.getText(None, __doc__, "Template Tag to Load:", text='foo bar')[0]).strip() + ' %} ')
        elif action in 'now':
            self.locator.get_service("editor").insert_text('{% now "' + str(QInputDialog.getItem(None, __doc__, "Current Date Time format:", ['DATETIME_FORMAT', 'SHORT_DATETIME_FORMAT', 'SHORT_DATE_FORMAT', 'DATE_FORMAT'], 0, False)[0]) + '" %} ')
        elif action in 'regroup':
            self.locator.get_service("editor").insert_text('{% regroup ' + str(QInputDialog.getText(None, __doc__, "Regroup a list of alike objects by a common attribute:", text='cities by country as country_list')[0]).strip() + ' %} ')
        elif action in 'spaceless':
            self.locator.get_service("editor").insert_text('{% spaceless %} ' + str(self.locator.get_service("editor").get_actual_tab().textCursor().selectedText().encode("utf-8")) + ' {% endspaceless %}')
        elif action in 'ssi':
            self.locator.get_service("editor").insert_text('{% ssi "' + str(QInputDialog.getText(None, __doc__, "Full Path to Template to Include:", text='/tmp/template.html')[0]).strip() + '" parsed %} ')
        elif action in 'ssifile':
            self.locator.get_service("editor").insert_text('{% ssi "' + str(path.abspath(QFileDialog.getOpenFileName(None, "{} - Open File".format(__doc__), path.expanduser("~"), '*.*(*.*)'))).strip() + '" parsed %} ')
        elif action in 'templatetag':
            self.locator.get_service("editor").insert_text('{% templatetag ' + str(QInputDialog.getItem(None, __doc__, "Template Tag tags:", ['openblock', 'openvariable', 'openbrace', 'opencomment'], 0, False)[0]) + ' %} ' + str(self.locator.get_service("editor").get_actual_tab().textCursor().selectedText().encode("utf-8")) + '{% templatetag ' + str(QInputDialog.getItem(None, __doc__, "Template Tag tags:", ['closeblock', 'closevariable', 'closebrace', 'closecomment'], 0, False)[0]) + ' %} ')
        elif action in 'url':
            self.locator.get_service("editor").insert_text('{% url ' + str(QInputDialog.getText(None, __doc__, "View method name string and optional variables:", text='"path.to.some_view" variable1 variable2')[0]).strip() + ' %} ')
        elif action in 'verbatim':
            self.locator.get_service("editor").insert_text('{% verbatim %} ' + str(self.locator.get_service("editor").get_actual_tab().textCursor().selectedText().encode("utf-8")) + ' {% endverbatim %}')
        elif action in 'widthratio':
            self.locator.get_service("editor").insert_text(' {% widthratio' + ' {} {} {} '.format(QInputDialog.getText(None, __doc__, "Variable or String to use as Value:", text='variable')[0], QInputDialog.getText(None, __doc__, "Variable or String to use as Maximum Value:", text='max_value')[0], QInputDialog.getText(None, __doc__, "Variable or String to use as Maximum Width:", text='max_width')[0]) + ' %} ')
        elif action in 'with':
            self.locator.get_service("editor").insert_text(' {% width ' + str(QInputDialog.getText(None, __doc__, "One or Multiple Variables to Cache on the View, key=value space separated:", text='variable1=foo.bar variable2=bar.baz')[0]).strip() + ' %} ' + str(self.locator.get_service("editor").get_actual_tab().textCursor().selectedText().encode("utf-8")) + ' {% endwidth %}')
        elif action in 'add':
            self.locator.get_service("editor").insert_text('|add:{} '.format(QInputDialog.getText(None, __doc__, "Variable or String to Add:", text='variable')[0]))
        elif action in 'addslashes':
            self.locator.get_service("editor").insert_text('|addslashes ')
        elif action in 'capfirst':
            self.locator.get_service("editor").insert_text('|capfirst ')
        elif action in 'center':
            self.locator.get_service("editor").insert_text('|center:"{}" '.format(int(QInputDialog.getInteger(None, __doc__, "Number of spaces to center:", 10, 1, 99, 1)[0])))
        elif action in 'cut':
            self.locator.get_service("editor").insert_text('|cut:"{}" '.format(QInputDialog.getText(None, __doc__, "Characters to Cut:", text=' ')[0]))
        elif action in 'date':
            self.locator.get_service("editor").insert_text('|date:"' + str(QInputDialog.getItem(None, __doc__, "Date Time format:", ['DATETIME_FORMAT', 'SHORT_DATETIME_FORMAT', 'SHORT_DATE_FORMAT', 'DATE_FORMAT'], 0, False)[0]) + '" ')
        elif action in 'default':
            self.locator.get_service("editor").insert_text('|default:"{}" '.format(QInputDialog.getText(None, __doc__, "String if evaluates as False:", text='nothing')[0]))
        elif action in 'default_if_none':
            self.locator.get_service("editor").insert_text('|default_if_none:"{}" '.format(QInputDialog.getText(None, __doc__, "String if None:", text='nothing')[0]))
        elif action in 'dictsort':
            self.locator.get_service("editor").insert_text('|dictsort:"{}" '.format(QInputDialog.getText(None, __doc__, "Sort List of Dicts by given Key:", text='key')[0]))
        elif action in 'dictsortreversed':
            self.locator.get_service("editor").insert_text('|dictsortreversed:"{}" '.format(QInputDialog.getText(None, __doc__, "Sort and Reverse List of Dicts by given Key:", text='key')[0]))
        elif action in 'divisibleby':
            self.locator.get_service("editor").insert_text('|divisibleby:"{}" '.format(int(QInputDialog.getInteger(None, __doc__, "Return True if its Divisible by:", 10, 1, 99, 1)[0])))
        elif action in 'escape':
            self.locator.get_service("editor").insert_text('|escape ')
        elif action in 'escapejs':
            self.locator.get_service("editor").insert_text('|escapejs ')
        elif action in 'filesizeformat':
            self.locator.get_service("editor").insert_text('|filesizeformat ')
        elif action in 'first':
            self.locator.get_service("editor").insert_text('|first ')
        elif action in 'fix_ampersands':
            self.locator.get_service("editor").insert_text('|fix_ampersands ')
        elif action in 'floatformat':
            self.locator.get_service("editor").insert_text('|floatformat:"{}" '.format(int(QInputDialog.getInteger(None, __doc__, "How many Decimals:", 10, 1, 99, 1)[0])))
        elif action in 'force_escape':
            self.locator.get_service("editor").insert_text('|force_escape ')
        elif action in 'get_digit':
            self.locator.get_service("editor").insert_text('|get_digit:"{}" '.format(int(QInputDialog.getInteger(None, __doc__, "Return string index of integer digit:", 10, 1, 99, 1)[0])))
        elif action in 'iriencode':
            self.locator.get_service("editor").insert_text('|iriencode ')
        elif action in 'join':
            self.locator.get_service("editor").insert_text('|join:"{}" '.format(QInputDialog.getText(None, __doc__, "Join values by:", text='//')[0]))
        elif action in 'last':
            self.locator.get_service("editor").insert_text('|last ')
        elif action in 'lenght':
            self.locator.get_service("editor").insert_text('|lenght ')
        elif action in 'lenght_is':
            self.locator.get_service("editor").insert_text('|lenght_is:"{}" '.format(int(QInputDialog.getInteger(None, __doc__, "Return True is lenght is:", 10, 1, 99, 1)[0])))
        elif action in 'linebreaks':
            self.locator.get_service("editor").insert_text('|linebreaks ')
        elif action in 'linebreaksbr':
            self.locator.get_service("editor").insert_text('|linebreaksbr ')
        elif action in 'linenumbers':
            self.locator.get_service("editor").insert_text('|linenumbers ')
        elif action in 'ljust':
            self.locator.get_service("editor").insert_text('|ljust:"{}" '.format(int(QInputDialog.getInteger(None, __doc__, "How many Spaces to Justify to the Left:", 10, 1, 99, 1)[0])))
        elif action in 'lower':
            self.locator.get_service("editor").insert_text('|lower ')
        elif action in 'make_list':
            self.locator.get_service("editor").insert_text('|make_list ')
        elif action in 'phone2numeric':
            self.locator.get_service("editor").insert_text('|phone2numeric ')
        elif action in 'pluralize':
            self.locator.get_service("editor").insert_text('|pluralize ')
        elif action in 'pprint':
            self.locator.get_service("editor").insert_text('|pprint ')
        elif action in 'random':
            self.locator.get_service("editor").insert_text('|random ')
        elif action in 'removetags':
            self.locator.get_service("editor").insert_text('|removetags:"{}" '.format(QInputDialog.getText(None, __doc__, "HTML Tags to remove, space separated:", text='b strong')[0]))
        elif action in 'rjust':
            self.locator.get_service("editor").insert_text('|rjust:"{}" '.format(int(QInputDialog.getInteger(None, __doc__, "How many Spaces to Justify to the Right:", 10, 1, 99, 1)[0])))
        elif action in 'safe':
            self.locator.get_service("editor").insert_text('|safe ')
        elif action in 'safeseq':
            self.locator.get_service("editor").insert_text('|safeseq ')
        elif action in 'slice':
            self.locator.get_service("editor").insert_text('|slice:"{}" '.format(QInputDialog.getText(None, __doc__, "Perform Python like Slice by:", text=':5')[0]))
        elif action in 'slugify':
            self.locator.get_service("editor").insert_text('|slugify ')
        elif action in 'stringformat':
            self.locator.get_service("editor").insert_text('|stringformat:"{}" '.format(QInputDialog.getText(None, __doc__, "Perform Python like String Format:")[0]))
        elif action in 'striptags':
            self.locator.get_service("editor").insert_text('|striptags ')
        elif action in 'time':
            self.locator.get_service("editor").insert_text('|time:"' + str(QInputDialog.getItem(None, __doc__, "Date Time format:", ['DATETIME_FORMAT', 'SHORT_DATETIME_FORMAT', 'SHORT_DATE_FORMAT', 'DATE_FORMAT'], 0, False)[0]) + '" ')
        elif action in 'timesince':
            self.locator.get_service("editor").insert_text('|timesince ')
        elif action in 'timeuntil':
            self.locator.get_service("editor").insert_text('|timeuntil ')
        elif action in 'title':
            self.locator.get_service("editor").insert_text('|title ')
        elif action in 'truncatechars':
            self.locator.get_service("editor").insert_text('|truncatechars:{} '.format(int(QInputDialog.getInteger(None, __doc__, "Truncate by how many Chars:", 10, 1, 99, 1)[0])))
        elif action in 'truncatewords':
            self.locator.get_service("editor").insert_text('|truncatewords:{} '.format(int(QInputDialog.getInteger(None, __doc__, "Truncate by how many Words:", 10, 1, 99, 1)[0])))
        elif action in 'truncatewords_html':
            self.locator.get_service("editor").insert_text('|truncatewords_html:{} '.format(int(QInputDialog.getInteger(None, __doc__, "Truncate by how many Words with HTML:", 10, 1, 99, 1)[0])))
        elif action in 'unordered_list':
            self.locator.get_service("editor").insert_text('|unordered_list ')
        elif action in 'upper':
            self.locator.get_service("editor").insert_text('|upper ')
        elif action in 'urlencode':
            self.locator.get_service("editor").insert_text('|urlencode ')
        elif action in 'urlize':
            self.locator.get_service("editor").insert_text('|urlize ')
        elif action in 'urlizetrunc':
            self.locator.get_service("editor").insert_text('|urlizetrunc ')
        elif action in 'wordcount':
            self.locator.get_service("editor").insert_text('|wordcount ')
        elif action in 'wordwrap':
            self.locator.get_service("editor").insert_text('|wordwrap:{} '.format(int(QInputDialog.getInteger(None, __doc__, "Wrap by how many Words:", 10, 1, 99, 1)[0])))
        elif action in 'yesno':
            self.locator.get_service("editor").insert_text('|yesno:"{}" '.format(QInputDialog.getText(None, __doc__, "Maps values for True, False and (optionally) None, to Strings:", text='yes,no,maybe')[0]))
        elif action in 'apnumber':
            self.locator.get_service("editor").insert_text(' | apnumber ')
        elif action in 'intcomma':
            self.locator.get_service("editor").insert_text(' | intcomma ')
        elif action in 'intword':
            self.locator.get_service("editor").insert_text(' | intword ')
        elif action in 'naturalday':
            self.locator.get_service("editor").insert_text(' | naturalday ')
        elif action in 'naturaltime':
            self.locator.get_service("editor").insert_text(' | naturaltime ')
        elif action in 'ordinal':
            self.locator.get_service("editor").insert_text(' | ordinal ')
        elif action in 'lorem':
            self.locator.get_service("editor").insert_text('{% lorem ' + str(int(QInputDialog.getInteger(None, __doc__, "Number of paragraphs or words to generate:", 10, 1, 99, 1)[0])) + ' p %}')
        elif action in 'static':
            self.locator.get_service("editor").insert_text('{% static "' + str(QInputDialog.getText(None, __doc__, "Relative Path to Static File:", text='img/icon.png')[0]).strip() + '" %} ')
        elif action in 'staticfile':
            self.locator.get_service("editor").insert_text('{% static "' + str(path.abspath(QFileDialog.getOpenFileName(None, "{} - Open File".format(__doc__), path.expanduser("~"), '*.*(*.*)'))).strip() + '" %} ')
        elif action in 'get_static_prefix':
            self.locator.get_service("editor").insert_text('{% get_static_prefix %}')
        elif action in 'get_media_prefix':
            self.locator.get_service("editor").insert_text('{% get_media_prefix %}')
        elif action in 'singlelinecomment':
            self.locator.get_service("editor").insert_text('{# ' + str(self.locator.get_service("editor").get_actual_tab().textCursor().selectedText().encode("utf-8")) + ' #}')
        elif action in 'multilinecomment':
            self.locator.get_service("editor").insert_text('{% comment %} ' + str(self.locator.get_service("editor").get_actual_tab().textCursor().selectedText().encode("utf-8")) + ' {% endcomment %}')
        elif action in 'singlelinecommentpopup':
            self.locator.get_service("editor").insert_text('{# ' + str(QInputDialog.getText(None, __doc__, "Type a New Django Template Comment:")[0]).strip() + ' #}')
        elif action in 'multilinecommentpopup':
            dialog, group0, stringy = QDialog(), QGroupBox(), QTextEdit()
            group0.setTitle(__doc__)
            button, glow = QPushButton(' OK '), QGraphicsDropShadowEffect()
            button.setMinimumSize(200, 50)
            button.clicked.connect(lambda: self.locator.get_service("editor").insert_text('{% comment %} ' + str(stringy.toPlainText()).strip() + ' {% endcomment %}'))
            button.released.connect(lambda: dialog.close())
            glow.setOffset(0)
            glow.setBlurRadius(99)
            glow.setColor(QColor(99, 255, 255))
            button.setGraphicsEffect(glow)
            vboxg0 = QVBoxLayout(group0)
            for each_widget in (QLabel('<b>Multiline Comment'), stringy, button):
                vboxg0.addWidget(each_widget)
            QVBoxLayout(dialog).addWidget(group0)
            dialog.show()
        elif action in 'singlelinecommentclipboard':
            self.locator.get_service("editor").insert_text('{# ' + str(QApplication.clipboard().text().encode("utf-8")).strip() + ' #}')
        elif action in 'multilinecommentclipboard':
            self.locator.get_service("editor").insert_text('{% comment %} ' + str(QApplication.clipboard().text().encode("utf-8")).strip() + ' {% endcomment %}')
        elif action in 'multilinecommentfile':
            with open(path.abspath(QFileDialog.getOpenFileName(None, "{} - Open File".format(__doc__), path.expanduser("~"), '*.*(*.*)')),  'r') as f:
                self.locator.get_service("editor").insert_text('{% comment %} ' + f.read() + ' {% endcomment %}')
        elif action in 'singlelinecommentdatetime':
            self.locator.get_service("editor").insert_text('{# ' + datetime.now().isoformat().split('.')[0] + ' by ' + getuser() + ' #}')
        #elif action in 'i18n':
            #pass
        #elif action in 'l10n':
            #pass
        #elif action in 'tz':
            #pass


###############################################################################


if __name__ == "__main__":
    print(__doc__)
