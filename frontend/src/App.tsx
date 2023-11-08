import {
  Admin,
  Resource,
  ListGuesser,
  Create, SimpleForm, TextInput, FileInput, FileField
} from "react-admin";
import { dataProvider } from "./dataProvider";

const DockerfileCreate = () => (
  <Create>
      <SimpleForm>
          <TextInput source="tag_name" />
          <FileInput source="dockerfile" >
            <FileField source="src" title="title" />
          </FileInput>
      </SimpleForm>
  </Create>
);

export const App = () => (
  <Admin dataProvider={dataProvider}>
    <Resource
      name="dockerfiles"
      list={ListGuesser}
      create={DockerfileCreate}
    />
  </Admin>
);
