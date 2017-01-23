# 192. Word Frequency
#
# @date: 2017/01/24
# Read from the file words.txt and output the word frequency list to stdout.
awk '{
	for(i=1; i<=NF; i++) 
		counts[$i]++
	} END {
		for(word in counts) 
		print word, counts[word]
	}' words.txt | sort -k2 -nr