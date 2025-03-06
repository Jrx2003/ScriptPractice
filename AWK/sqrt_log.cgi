#!/usr/bin/awk -f

BEGIN {
	print "Content-type: text/html\n"
	query = ENVIRON["QUERY_STRING"]

	# Parse parameters
	split(query, params, "&")
	for (i in params) {
		split(params[i], pair, "=")
		key = pair[1]
		value = pair[2]
		# Clean up URL encoding
		gsub(/\+/, " ", value)
		gsub(/%[0-9A-Fa-f][0-9A-Fa-f])/, "", value)
		if (key == "number") number = value
		if (key == "operation") operation = value
	}

	# Perform the selected operation
	if (operation == "log2" ) {
		result = log(number) / log(2)
	} else if (operation == "log10") {
		result = log(number) / log(10)
	} else if (operation == "sqrt") {
		result = sqrt(number)
	} else {
		print ("<html><body><p>INVALID OPERATION!</p></body></html>")
		exit
	}

	# Print the result
	print("<html><body><p>Result: " result "</p></body></html>")
}	