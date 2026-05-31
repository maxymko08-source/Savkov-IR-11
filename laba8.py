def find_max_chain_with_bucket_sort(words_list):
    words_set = set(words_list)

    buckets = [[] for _ in range(51)]

    for word in words_list:
        word_len = len(word)
        if word_len <= 50:
            buckets[word_len].append(word)

    sorted_words = []
    for bucket in buckets:
        sorted_words.extend(bucket)

    dp = {}
    max_chain_length = 0

    for word in sorted_words:
        current_max = 1
        
        for i in range(len(word)):
            smaller_word = word[:i] + word[i+1:]
            
            if smaller_word in words_set:
                if smaller_word in dp:
                    current_max = max(current_max, dp[smaller_word] + 1)
        
        dp[word] = current_max
        if current_max > max_chain_length:
            max_chain_length = current_max

    return max_chain_length