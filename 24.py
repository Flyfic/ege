# s = open('24_2497.txt').readline()
# print(s.count('XVIII'))
# k=0
# for i in range(len(s)-4):
# 	if s[i:i+5] == 'XVIII':
# 		k+=1
# print(k)

# s = open('24_223.txt').readline()
# print(s.count('TIK')+s.count('TOK'))

# s = open('24_314.txt').readline()
# print(s.count('OCK')-s.count('STOCK'))

# s = open('24_279.txt').readline()
# print(s.count('BOSS')-s.count('JBOSS')-s.count('BOSSJ')+s.count('JBOSSJ'))

# s = open('24_2498.txt').readline()
# while 'XIXIX' in s:
# 	s = s.replace('XIXIX','XIX XIX')
# print(s.count('XIX'))
# k=0
# for i in range(len(s)-2):
# 	if s[i:i+3]=='XIX':
# 		k+=1
# print(k)

# s = open('24_2499.txt').readline()
# while 'XXXXX' in s:
# 	s = s.replace('XXXXX','XXXX XXXX')
# print(s.count('XXXX'))

# s = open('24_2500.txt').readline()
# k=0
# for i in range(len(s)-3):
# 	if s[i]=='G' and s[i+2]=='M' and s[i+3]=='E':
# 		k+=1
# print(k)
# k1 = 0
# for x in 'QWERTYUIOPASDFGHJKLZXCVBNM':
# 	k1+=s.count(f'G{x}ME')
# print(k1)

# s = open('24_2501.txt').readline()
# k = 0
# for i in range(len(s)-4):
# 	if s[i]=='A' and s[i+2]=='A' and s[i+4]=='A':
# 		k+=1
# print(k)
# k = 0
# for s in open('24_859.txt'):
# 	if s.count('S') == s.count('X'):
# 		k+=1
# print(k)

# k = 0
# for s in open('24_587.txt'):
# 	if s.count('B')-s.count('A')>=s.count('A')*0.05:
# 		k+=1
# print(k)

# k = 0
# for s in open('24_2502.txt'):
# 	k1 = 0
# 	for i in range(len(s)-3):
# 		if s[i]=='K' and s[i+2]=='G' and s[i+3]=='E':
# 			k1+=1
# 	if k1 > 0:
# 		k += 1
# print(k)

# k = 0
# for s in open('24_2503.txt'):
# 	x = 0
# 	y = 0
# 	for i in range(len(s)-2):
# 		if s[i:i+3]=='AOA':
# 			x+=1
# 		if s[i:i+3]=='OAO':
# 			y+=1
# 	if x > y:
# 		k+=1
# print(k)

# s = open('24_1143.txt').readline()
# c=0
# for k in range(6,10):
# 	for j in range(len(s)-k):
# 		if s[j]=='A' and s[j+k] == 'F':
# 			c+=1
# print(c)

# s = open('24_836.txt').readline()
# k = 0
# for i in range(len(s)-4):
# 	if s[i:i+5]==s[i+4:i-1:-1]:
# 		k+=1
# print(k)

# s = open('24_2506.txt').readline().strip()
# d = {x:s.count(x) for x in sorted(set(s))}
# m = 0
# c = ''
# for x in d:
# 	if d[x]>m:
# 		m = d[x]
# 		c = x
# print(c,m)
# print(d)

# s = open('24_2509.txt').readline().strip()
# d = {x:s.count(x) for x in sorted(set(s))}
# print(max(d.values())-min(d.values()))

# s = open('24_2505.txt').readline().strip()
# d = {x:0 for x in sorted(set(s))}
# for i in range(len(s)-2):
# 	if s[i]==s[i+2]:
# 		d[s[i+1]]+=1
# print([x for x in d if d[x]==max(d.values())],max(d.values()))

# s = open('24_2504.txt').readline().strip()
# d = {x:0 for x in sorted(set(s))}
# for i in range(len(s)-4):
# 	if s[i:i+2]=='CB' and s[i+3:i+5]=='BC':
# 		d[s[i+2]]+=1
# mx = max(d.values())
# print([i for i in d if d[i]==mx],mx)

# k=0
# s1 = ''
# ss = ''
# for s in open('24_2508.txt'):
# 	if s.count('Q')>=k:
# 		k = s.count('Q')
# 		s1 = s
# 	ss+=s
# s1 = s1.strip()
# d = {x:s1.count(x) for x in sorted(set(s1))}
# m = 10**10
# c = ''
# for x in d:
# 	if d[x]<m:
# 		m = d[x]
# 		c = x
# print(c,ss.count(c))

# for s in open('24_2507.txt'):
# 	d = {x:1 x for x in sorted(set(s))}
# 	for i in range(len(s)-1):
# 		if s[i]==s[i+1]:
# 			d[s[i]]+=1
# 		else:
# 			d[s[i]]

# s = open('24_9552.txt').readline()
# while 'PCSGO' in s:
# 	s = s.replace('PCSGO','PC CSGO')
# s = s.replace('PC','**').replace('CSGO','****')
# for x in 'QWERTYUIOPASDFGHJKLZXCVBNM':
# 	s = s.replace(x,' ')
# print(max(len(x) for x in s.split()))

# s = open('24_9552.txt').readline()
# m = [0]*len(s)
# for i in range(1,len(s)):
# 	if s[i-1]+s[i]=='PC':
# 		m = m[i-2]+2
# 	if i >= 3 and s[i-3:i+1]:
# 		m = m[i-4]+4
# print(max(m))

# s = open('24_4546.txt').readline()
# m = [0]*len(s)
# for i in range(2,len(s)):
# 	if s[i-2] == s[i] and s[i] in 'AC':
# 		m[i] = m[i-3]+1
# print(max(m))

# s = open('24_2426.txt').readline()
# s = s.replace('A',' ').replace('B',' ').replace('C',' ')
# c = s.split()
# print(max(len(x) for x in c))

# s = open('24_1040.txt').readline()
# for x in 'qwertyuiopasdfghjklzxcvbnm':
# 	s = s.replace(x,' ')
# print(max(len(c) for c in s.split()))

# s = open('24_1428.txt').readline()
# s = s.replace('XY','X Y').replace('XZ','X Z')
# print(max(len(c) for c in s.split()))  #Разбиваем подстроку, т.к считаем максимально кол-во идущих подряд символом

# s = open('24_1975.txt').readline()
# while 'PP' in s:
# 	s = s.replace('PP','P P')
# print(max(len(c) for c in s.split()))

# s = open('24_1302.txt').readline()
# s = s.replace('XZZY','XZZ ZZY')
# print(max(len(c) for c in s.split()))

# s = open('24_4627.txt').readline()
# s = s.replace('NPO','*').replace('PNO','*')
# s = s.replace('N',' ').replace('O',' ').replace('P',' ')
# print(max(len(c) for c in s.split()))

# s = open('24_4643.txt').readline()
# s = s.replace('B','A').replace('2','1')
# s = s.replace('11A','*')
# s = s.replace('A',' ').replace('1',' ')
# print(max(len(c) for c in s.split()))

# s = open('24_8510.txt').readline()
# for x in 'NOP':
# 	for y in 'NOP':
# 		while x+y in s:
# 			s = s.replace(x+y, f'{x} {y}')
# print(max(len(c) for c in s.split()))

# s = open('24_21.txt').readline()
# m = [1]*len(s)
# for i in range(1,len(s)):
# 	if s[i]!=s[i-1]:
# 		m[i] = m[i-1]+1
# print(max(m))

# s = open('24_2422.txt').readline()
# m = [1]*len(s)
# for i in range(1,len(s)):
# 	if s[i] >= s[i-1]:
# 		m[i]= m[i-1]+1
# print(max(m))

# s = open('24_2423.txt').readline()
# m = [1]*len(s)
# for i in range(1,len(s)):
# 	if s[i]>s[i-1]:
# 		m[i]=m[i-1]+1
# print(max(m))

# s = open('24_2427.txt').readline()
# m = [1]*len(s)
# for i in range(1,len(s)):
# 	if s[i]<s[i-1]:
# 		m[i]=m[i-1]+1
# 	if m[i]==9:
# 		print(s[i-8:i+1])

# s = open('24_4113.txt').readline()
# m = [0]*len(s)
# for i in range(1,len(s)):
# 	if s[i-1]+s[i]=='BB' or s[i-1]+s[i]=='DD':
# 		m[i] = m[i-2]+1
# print(max(m))

# s = open('24_9552.txt').readline()
# m = [0]*len(s)
# for i in range(1,len(s)):
# 	if s[i-1]+s[i]=='PC':
# 		m[i] = m[i-2]+2
# 	if s[i-3:i+1]=='CSGO':
# 		m[i] = m[i-4]+4
# print(max(m))

# s = open('24_4546.txt').readline()
# m = [0]*len(s)
# for i in range(2,len(s)):
# 	if s[i-2]==s[i] and s[i] in 'AC':
# 		m[i]=m[i-3]+1
# print(max(m))

# s = open('24_2251.txt').readline()
# l = k = m = 0
# for r in range(len(s)):
# 	if s[r]=='D':
# 		k+=1
# 	while k>2:
# 		if s[l]=='D':
# 			k-=1
# 		l+=1
# 	m = max(m,r-l+1)
# print(m)

# s = open('24_10105.txt').readline()
# l = m = k = 0
# for r in range(len(s)):
# 	if s[r] == 'T':
# 		k+=1
# 	while k>100:
# 		if s[l]=='T':
# 			k-=1
# 		l+=1
# 	m = max(m,r-l+1)
# print(m)

# s = open('24_13715.txt').readline()
# l = k = m = 0
# for r in range(1,len(s)):
# 	if s[r-1] + s[r]=='AB':
# 		k+=1
# 	while k > 50:
# 		if s[l]+s[l+1]=='AB':
# 			k-=1
# 		l+=1
# 	if k==50:
# 		m = max(m,r-l+1)
# print(m)

# s = open('24_12476.txt').readline()
# l = m = k = 0
# for r in range(1,len(s)):
# 	if s[r-1]+s[r]=='RO':
# 		k+=1
# 	if s[r-2:r+1]=='ORO' or s[r-2:r+1] == 'ROR':
# 		l = r
# 		k = 0
# 	while k > 21:
# 		if s[l]+s[l+1]=='RO':
# 			k-=1
# 		l+=1
# 	if k == 21:
# 		m = max(m,r-l+1)
# print(m)

# s = open('24_6734.txt').readline()
# l = k = 0
# m = 10**5
# for r in range(len(s)):
# 	if s[r] == '.':
# 		k += 1
# 	while k >= 7:
# 		if s[l] == '.':
# 			k-= 1
# 		l += 1
# 		if k == 7:
# 			m = min(m,r-l+1)
# print(m)

# s = open('24_11954.txt').readline()
# l = kx = 0
# m = 100000
# for r in range(len(s)):
# 	if s[r] == 'X':
# 		kx += 1
# 	if s[r] == 'Y':
# 		l = r+1
# 		kx = 0
# 	while kx == 500:
# 		m = min(m,r-l+1)
# 		if s[l]=='X':
# 			kx-=1
# 		l+=1
# print(m)

# s = open('24_9169.txt').readline()
# k = l = 0
# m = 100000
# for r in range(2,len(s)):
# 	if s[r-2:r+1] == 'BAD' or s[r-2:r+1]=='FAT':
# 		k+=1
# 	while k == 3:
# 		m = min(m,r-l+1)
# 		if s[l:l+3]=='BAD' or s[l:l+3]=='FAT':
# 			k-=1
# 		l+=1
# print(m)

# s = open('24_5171.txt').readline()
# l = m = k = 0
# for r in range(1,len(s),2):
# 	if s[r-1]+s[r]=='CA':
# 		k+=2
# 	else: 
# 		m = max(m,k)
# 		k = 0
# print(m)

# s = open('24_2425.txt').readline()
# print('DBAC'*23+'DBAC' in s)
# print(4*23+3)

s = open('24_2428.txt').readline()
print('YZ'+'XYZ'*22+'X' in s)
print(3*22+1+2)











