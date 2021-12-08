lines = None
with open('day 8/day8.txt') as infile:
    lines = [x.rstrip('\n') for x in infile]

lines = [x.split(' | ') for x in lines]
direct_map = {2: 1, 3: 7, 4: 4, 7: 8, 6: (6,9,0), 5: (2,5,3)}

result = 0
for input, output in lines:
    input = input.split(" ")
    mapper = {}
    for digit_segments in input:
        if len(digit_segments) in {2,3,4,7}: # 1, 4, 7, 8
            mapper[direct_map[len(digit_segments)]] = set(digit_segments)
    for digit_segments in input:
        digit_segments = set(digit_segments)
        if len(digit_segments) == 5: # 2,3,5
            if mapper[7].issubset(digit_segments):
                mapper[3] = digit_segments
            else:
                four_segs = mapper[4]
                one_segs = mapper[1]
                is_2 = False
                for off_segment in (mapper[8] - digit_segments):
                    if off_segment in four_segs and not off_segment in one_segs:
                        is_2 = True
                        break
                mapper[2 if is_2 else 5] = digit_segments
        elif len(digit_segments) == 6: # 6,9,0
            if mapper[4].issubset(digit_segments):
                mapper[9] = digit_segments
            else:
                off_segment = mapper[8] - digit_segments
                if off_segment.issubset(mapper[4]) and not off_segment.issubset(mapper[1]):
                    mapper[0] = digit_segments
                else:
                    mapper[6] = digit_segments
    trans_dict = {frozenset(v): k for k, v in mapper.items()}
    power = 3
    output_value = 0
    for segments in output.split():
        output_value += trans_dict[frozenset(segments)] * 10**power
        power -= 1
    result += output_value

    
print(result)

