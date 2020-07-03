# I'm posting all the stuff I've found on forums here so I can refer back to it when I need help #

I'll need the svgutils package, but you can combine two svg files and layer one on top of the other

>
>
>
> template = st.fromfile('images/test.svg')
>
> second_svg = st.fromfile('images/test2.svg')
>
> template.append(second_svg)
>
> template.save('images/merged.svg')
>
remember to save each of the files before loading them in with svgutils

