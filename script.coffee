jQuery(document).ready ->
    answer = () ->
        question = jQuery("#question").val()
        alert(question)
        
    jQuery("#ask").click( (event) ->
        event.preventDefault()
        answer() )
                        
    # Doesn't look like following is needed as firefox fires the
    # button click when enter pressed on the input field
    #jQuery("#question").keydown( (event) ->
        #if event.which == 13
            #answer() )