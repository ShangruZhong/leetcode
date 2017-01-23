# 194. Transpose File
#
# @date: 2017/01/24
# Read from the file file.txt and print its transposed content to stdout.
awk '{
for(i = 1; i <= NF; i++) {
    if(line[i] == "") {
        line[i] = $i
    } else {
        line[i] = line[i] " " $i
    }
    }
}
END {
    for(i = 1; line[i] != ""; i++) {
        print line[i];
    }
}' file.txt