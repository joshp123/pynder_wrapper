<%inherit file="pynder_web:templates/base.mako" />

<div class="page-header">
    <h1>likes test</h1>
</div>

<div class="user_id" id=${user.id}></div>

<button type="button" class="btn btn-success" onclick=choose("like")>Like</button>
<button type="button" class="btn btn-info" onclick=choose("superlike")>Superlike</button>
<button type="button" class="btn btn-warning" onclick=choose("nope")>Nope</button>



<%include file="pynder_web:/templates/expanded_user.mako"/>

<script type="text/javascript">
    choose = function(choice) {
        $.ajax({
            type: 'POST',
            url: '/likes/${user.id}/' + choice + '/',
            data: '',
            success: function(response) {
                console.log(response);
                window.location.reload();
                // TODO: maybe refresh the session? 
            }
        })
    };
</script>
