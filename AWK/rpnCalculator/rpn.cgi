#!/usr/bin/awk -f
#
# Minimal RPN script with debug info to show how "3 4 +" is being parsed.
# Only supports "+" and "-" operations.

BEGIN {
    # 1) Print HTTP header
    print "Content-type: text/html\n"

    # 2) Grab the GET query
    query = ENVIRON["QUERY_STRING"]  # e.g. "expression=3+4+%2B"

    # Debug: let's keep a copy
    rawQuery = query

    expression = ""

    # 3) Parse the query for "expression=..."
    split(query, parts, "&")
    for (i in parts) {
        split(parts[i], kv, "=")
        key = kv[1]
        val = kv[2]
        if (key == "expression") {
            expression = val
        }
    }

    # Debug: Save the raw expression from the URL
    rawExpression = expression

    # 4) Basic decoding
    #    a) Replace '+' with space
    gsub(/\+/, " ", expression)

    #    a) Replace "%2B" with actual plus sign '+'
    #       (case-insensitive, so %2B / %2b / etc. all match)
    while (match(expression, /%2B/)) {
        expression = substr(expression, 1, RSTART-1) "+" substr(expression, RSTART+3)
    }

    #    c) Remove other %xx patterns (very naive)
    gsub(/%[0-9A-Fa-f]{2}/, "", expression)

    # Trim leading/trailing spaces
    gsub(/^ +| +$/, "", expression)

    # 5) Compute the RPN
    result = computeRPN(expression)

    # 6) Output HTML, plus some debug info
    print "<html><body>"
    print "<h3>RPN Calculator</h3>"
    print "<p><strong>Raw QUERY_STRING:</strong> " rawQuery "</p>"
    print "<p><strong>Raw expression param:</strong> " rawExpression "</p>"
    print "<p><strong>Decoded expression:</strong> " expression "</p>"
    print "<p><strong>Result:</strong> " result "</p>"
    print "</body></html>"

    exit
}

# computeRPN: supports '+' and '-' only
function computeRPN(expr,    tokens, n, stack, top, token, x, y) {
    n = split(expr, tokens, " ")
    top = 0

    for (i = 1; i <= n; i++) {
        token = tokens[i]
        # Skip empty tokens in case of extra spaces
        if (token == "") continue

        if (token == "+") {
            if (top < 2) return "Error: not enough operands"
            y = stack[top]
            x = stack[top-1]
            top -= 1
            stack[top] = x + y
        } else if (token == "-") {
            if (top < 2) return "Error: not enough operands"
            y = stack[top]
            x = stack[top-1]
            top -= 1
            stack[top] = x - y
        } else {
            # Assume it's a number
            top++
            stack[top] = token + 0
        }
    }

    if (top == 1) {
        return stack[1]
    }
    return "Error: invalid RPN (stack size=" top ")"
}
