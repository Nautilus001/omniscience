import graphene
from graphene_django import DjangoObjectType
from .models import Project, Container

class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = ("id", "name", "client", "status", "containers")

class ContainerType(DjangoObjectType):
    class Meta:
        model = Container
        fields = ("id", "name", "image", "status", "project")

class UpsertContainer(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        image = graphene.String(required=True)
        status = graphene.Boolean(required=True)
        project_id = graphene.Int(required=True)

    container = graphene.Field(ContainerType)

    def mutate(self, info, name, image, status, project_id):
        try:
            project = Project.objects.get(pk=project_id)
        except Project.DoesNotExist:
            raise Exception("Project not found!")

        container, created = Container.objects.update_or_create(
            name = name,
            project=project,
            defaults={'image': image, 'status': status}
        )

        return UpsertContainer(container=container)

class UpsertProject(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        client = graphene.String(required=True)
        status = graphene.Boolean(required=True)

    project = graphene.Field(ProjectType)

    def mutate(self, info, name, client, status):
        project, created = Project.objects.update_or_create(
            name = name,
            client=client,
            status=status
        )

        return UpsertProject(project=project)

class Mutation(graphene.ObjectType):
    upsert_container = UpsertContainer.Field()
    upsert_project = UpsertProject.Field()

class Query(graphene.ObjectType):
    all_projects = graphene.List(ProjectType)
    all_containers = graphene.List(ContainerType)

    def resolve_all_projects(self, info, **kwargs):
        return Project.objects.all()

    def resolve_all_containers(self, info, **kwargs):
        return Container.objects.all()

schema = graphene.Schema(query=Query, mutation = Mutation)