def mappreconcat(pref, lis):
    return map(lambda x: pref + x, lis)


pre = 'porco'
post = ['dio', 'cristo', 'madonno']
lis_new = list(mappreconcat(pre, post))
print(lis_new)
