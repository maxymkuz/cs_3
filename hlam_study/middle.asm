ebx - довжина масиву
edx - 

mov edi, ebx
jp func1

func1:
	cmp ebx, 0
	jnz func
	.....

func:
	add eax,  [edx + 4 * (edi - ebx)]
	sub ebx, 1
	jp func1