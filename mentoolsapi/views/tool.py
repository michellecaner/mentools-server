"""View module for handling requests about tools"""
from rest_framework.viewsets  import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from mentoolsapi.models import Tool

class ToolView(ViewSet):
    """Mentools tools view"""

    def retrieve(self, request, pk):
        """Handle a GET request for a tool"""
        tool =  Tool.objects.get(pk=pk)
        serializer = ToolSerializer(tool)
        return Response(serializer.data)

    def list(self, request):
        """Handle a GET request for all of the tools"""
        tools = Tool.objects.all()

        tool_type = request.query_params.get('type', None)
        if tool_type is not None:
            tools = tools.filter(tool_type_id=tool_type)

        serializer = ToolSerializer(tools, many=True)
        return Response(serializer.data)

class ToolSerializer(serializers.ModelSerializer):
    """JSON serializer for tools"""

    class Meta:
        model =  Tool
        fields = ('id', 'title', 'description', 'tool_type')