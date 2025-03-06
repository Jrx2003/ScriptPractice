#! /usr/bin/awk -f
BEGIN {
  print "Content-type: text/html\n"
  getline cgidat
  if (!cgidat) {
    loc = 1
    text = "~"
  } else process()
  genform()
}

func genform() {
    gsub(/\n*$/,"",text)
    print "length = " length(text)
    print "<hr>"
    print "<pre>"
    printf "%s", "<font id='pleft'>" substr(text,1,loc-1) "</font>"
    printf "%s", "<font style='background-color:yellow'><font id='pmid'>" substr(text,loc,1) "</font></font>"
    if (loc>0) printf "%s", "<font id='pright'>" substr(text,loc+1) "</font>"
    else printf "%s", "<font id='pright'>" substr(text,2) "</font>"
    print "</pre>"

    print "<hr>"

    print "<form method=post action=''>"

    print "<textarea name=text id=text cols=80 rows=20>"
    print text
    print "</textarea>"

    print "<script>"
    print "  myarea = document.getElementById('text');"
    print "  myarea.focus();"
    print "  myarea.setSelectionRange(" loc-1 "," loc ");"
    print "  myarea.addEventListener('click', function() { myloc = document.getElementById('loc'); myloc.value = myarea.selectionStart; makeconsistent(myarea); } );"
    print "  myarea.addEventListener('keydown', function() { makeconsistent(myarea); } );"
    print "  function makeconsistent(a) {"
    print "    aloc = parseInt(document.getElementById('loc').value);"
    print "    aval = document.getElementById('text').value;"
    print "    if (aloc>0) document.getElementById('pleft').innerHTML = aval.substring(0,aloc);"
    print "    else document.getElementById('pleft').innerHTML = '';"
    print "    document.getElementById('pmid').innerHTML = aval.substring(aloc,aloc+1);"
    print "    document.getElementById('pright').innerHTML = aval.substring(aloc+1);"
    print "  }"
    print "</script>"

    print "<input type=submit>"

    print "<br>"

    print "com: <input name=com id=com size=40 value=" com ">"
    print "<font size=-2 onclick='com.value=\"\";'> [clear] </font>"

    print "loc: <input name=loc id=loc size=6 value=" loc ">"

    # ---------------------------- WEEK 8 ----------------------------
    print "<br>"
    print "<input type='number' id='ddCount' placeholder='Lines to delete (n)' />"
    print "<button type='button' id='ddButton'>[n]dd</button>"

    print "<script>"
    print "  document.getElementById('ddButton').addEventListener('click', function() {"
    print "    let n = parseInt(document.getElementById('ddCount').value, 10);"
    print "    if (!n || n < 1) { n = 1; }"
    print "    let textarea = document.getElementById('text');"
    print "    let textVal = textarea.value;"
    print "    var lineStart = textVal.lastIndexOf('\\n', textarea.selectionStart - 1);"
    print "    lineStart = (lineStart === -1) ? 0 : lineStart + 1;"
    
    print "    var pos = lineStart;"
    print "    for (var i = 0; i < n; i++) {"
    print "      var nextNewline = textVal.indexOf('\\n', pos);"
    print "      if (nextNewline === -1) {"
    print "         pos = textVal.length;"
    print "         break;"
    print "      } else {"
    print "         pos = nextNewline + 1;"
    print "      }"
    print "    }"
    
    print "    let newText = textVal.substring(0, lineStart) + textVal.substring(pos);"
    print "    textarea.value = newText;"
    print "    if (lineStart >= newText.length) {"
    print "      lineStart = lineStart - 1;"
    print "    }"
    print "    textarea.selectionStart = textarea.selectionEnd = lineStart;"
    print "    document.getElementById('loc').value = lineStart;"
    print "    makeconsistent(textarea);"
    print "    textarea.focus();"
    print "  });"
    print "</script>"
    # ----------------------------------------------------------------

    print "</form>"
}

func process() {
  cleanandparse(cgidat)
  print "COM=/" com "/"
  if (com == "0") loc = 1
  if (com == "$") loc = length(text)-1
  if (com == "l") loc++
  if (com == "h") loc--
  if (com == "x") { print "DELETING /" substr(text,loc,1) "/ AT " loc; text = substr(text,1,loc-1) substr(text,loc+1) }
  if (com ~ "^/") { where = index(substr(text,loc+1), substr(com,2)); if (where) loc += where }

  if (com ~ /^[0-9]*dd$/) {
    n = 1
    if (match(com, /^[0-9]+/)) {
      n = substr(com, RSTART, RLENGTH) + 0
    }
    delete_lines(n)
  }

  if (loc < 0) loc = 0
  if (loc > length(text)) loc = length(text)
}

func delete_lines(n,   start, pos, i, newline_pos) {
    start = 1
    for (i = loc; i >= 1; i--) {
        if (substr(text, i, 1) == "\n") {
            start = i + 1
            break
        }
    }
    
    pos = start
    for (i = 0; i < n; i++) {
        newline_pos = index(substr(text, pos), "\n")
        if (newline_pos > 0) {
            pos += newline_pos
        } else {
            pos = length(text) + 1
            break
        }
    }
    
    text = substr(text, 1, start-1) substr(text, pos)
    loc = start
    if (loc >= length(text))
        loc = length(text) - 1
}

func cleanandparse(x,  i,temp,tt) {
  split(x,temp,/&/)
  for (i in temp) { split(temp[i], tt, /=/); dat[tt[1]] = tt[2] }
  gsub("%0D%0A","\n", dat["text"])
  gsub("+"," ", dat["text"])
  gsub("%3A",":", dat["text"])
  gsub("%2F","/", dat["com"])
  gsub("%24","$", dat["com"])
  com = dat["com"]
  loc = dat["loc"]
  text = dat["text"]
}

func htmlify(x) {
  # gsub("\n", "<br>", x)
  return x
}