jQuery(document).ready ->
    answer = () ->
        alert("do something here")
        
    jQuery("#ask").click( (event) ->
        event.preventDefault()
        answer() )
                        
    # Doesn't look like following is needed as firefox fires the
    # button click when enter pressed on the input field
    #jQuery("#question").keydown( (event) ->
        #if event.which == 13
            #answer() )